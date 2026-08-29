#!/usr/bin/env bash
set -uo pipefail

BASE_URL="${1:-}"

if [ -z "$BASE_URL" ]; then
  echo "Usage: $0 <revision-fqdn-or-url>"
  exit 2
fi

if [[ "$BASE_URL" != http://* && "$BASE_URL" != https://* ]]; then
  BASE_URL="https://${BASE_URL}"
fi

BASE_URL="${BASE_URL%/}"

FAILED=0
FAILED_CHECKS=()
FOUND_PRODUCT_ID=""

record_fail() {
  local NAME="$1"
  FAILED=1
  FAILED_CHECKS+=("$NAME")
}

http_get() {
  local ENDPOINT_PATH="$1"
  local OUTFILE="$2"

  curl --silent --show-error --location \
    --max-time 30 \
    --output "$OUTFILE" \
    --write-out "%{http_code}" \
    "$BASE_URL$ENDPOINT_PATH" \
    2>/tmp/validator_curl_error
}

check_status() {
  local NAME="$1"
  local ENDPOINT_PATH="$2"
  local EXPECTED="$3"
  local FOLLOW_REDIRECTS="${4:-false}"
  local OUTFILE
  OUTFILE=$(mktemp)

  echo ""
  echo "[CHECK] $NAME"
  echo "       $ENDPOINT_PATH"

  local CURL_ARGS=(--silent --show-error --max-time 30 --output "$OUTFILE" --write-out "%{http_code}")
  if [ "$FOLLOW_REDIRECTS" = "true" ]; then
    CURL_ARGS+=(--location)
  fi

  local CODE
  CODE=$(curl "${CURL_ARGS[@]}" "$BASE_URL$ENDPOINT_PATH" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ]; then
    echo "       FAIL: curl exit code $RC"
    cat /tmp/validator_curl_error 2>/dev/null || true
    record_fail "$NAME"
    rm -f "$OUTFILE"
    return 1
  fi

  echo "       HTTP $CODE (expected $EXPECTED)"
  if [ "$CODE" != "$EXPECTED" ]; then
    echo "       FAIL"
    record_fail "$NAME"
    rm -f "$OUTFILE"
    return 1
  fi

  echo "       PASS"
  echo "$OUTFILE"
  return 0
}

check_page_has_products() {
  local NAME="$1"
  local ENDPOINT_PATH="$2"
    local OUTFILE
  OUTFILE=$(mktemp)

  echo ""
  echo "[FUNCTIONAL] $NAME"
  echo "             $ENDPOINT_PATH"

  local CODE
  CODE=$(curl --silent --show-error --location --max-time 30 \
      --output "$OUTFILE" --write-out "%{http_code}" \
      "$BASE_URL$ENDPOINT_PATH" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ] || [ "$CODE" != "200" ]; then
    echo "             FAIL: HTTP $CODE / curl $RC"
    cat /tmp/validator_curl_error 2>/dev/null || true
    record_fail "$NAME"
    rm -f "$OUTFILE"
    return 1
  fi

  # The product list/detail pages use /products/<numeric-id> links.
  local PRODUCT_LINK
  PRODUCT_LINK=$(grep -oE 'href="/products/[0-9]+"' "$OUTFILE" | head -1 || true)

  if [ -z "$PRODUCT_LINK" ]; then
    echo "             FAIL: page returned 200 but contains no product links"
    record_fail "$NAME"
    rm -f "$OUTFILE"
    return 1
  fi

  FOUND_PRODUCT_ID=$(printf '%s' "$PRODUCT_LINK" | grep -oE '[0-9]+' | head -1)

  echo "             PASS: rendered product ID $FOUND_PRODUCT_ID"

  rm -f "$OUTFILE"
  return 0
}

check_product_detail() {
  local PRODUCT_ID="$1"
  local OUTFILE
  OUTFILE=$(mktemp)

  echo ""
  echo "[FUNCTIONAL] Product detail"
  echo "             /products/$PRODUCT_ID"

  local CODE
  CODE=$(curl --silent --show-error --location --max-time 30 \
      --output "$OUTFILE" --write-out "%{http_code}" \
      "$BASE_URL/products/$PRODUCT_ID" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ] || [ "$CODE" != "200" ]; then
    echo "             FAIL: HTTP $CODE / curl $RC"
    record_fail "product-detail"
    rm -f "$OUTFILE"
    return 1
  fi

  if ! grep -qiE 'Add to Cart|Price|Product' "$OUTFILE"; then
    echo "             FAIL: detail page returned 200 but expected product content was not found"
    record_fail "product-detail-content"
    rm -f "$OUTFILE"
    return 1
  fi

  echo "             PASS: product detail content rendered"
  rm -f "$OUTFILE"
}

check_category() {
  local CATEGORY="$1"
  local OUTFILE
  OUTFILE=$(mktemp)

  echo ""
  echo "[FUNCTIONAL] Category: $CATEGORY"

  local CODE
  CODE=$(curl --silent --show-error --location --max-time 30 \
      --output "$OUTFILE" --write-out "%{http_code}" \
      "$BASE_URL/products/category/$CATEGORY" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ] || [ "$CODE" != "200" ]; then
    echo "             FAIL: HTTP $CODE / curl $RC"
    record_fail "category-$CATEGORY"
    rm -f "$OUTFILE"
    return 1
  fi

  local PRODUCT_LINK
  PRODUCT_LINK=$(grep -oE 'href="/products/[0-9]+"' "$OUTFILE" | head -1 || true)
  if [ -z "$PRODUCT_LINK" ]; then
    echo "             FAIL: category page returned 200 but rendered no products"
    record_fail "category-$CATEGORY-content"
    rm -f "$OUTFILE"
    return 1
  fi

  echo "             PASS: category rendered at least one product"
  rm -f "$OUTFILE"
}

check_search() {
  local OUTFILE
  OUTFILE=$(mktemp)

  echo ""
  echo "[FUNCTIONAL] Product search"
  echo "             /products/?q=Pragmatic"

  local CODE
  CODE=$(curl --silent --show-error --location --max-time 30 \
      --output "$OUTFILE" --write-out "%{http_code}" \
      "$BASE_URL/products/?q=Pragmatic" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ] || [ "$CODE" != "200" ]; then
    echo "             FAIL: HTTP $CODE / curl $RC"
    record_fail "product-search"
    rm -f "$OUTFILE"
    return 1
  fi

  if ! grep -qi 'Pragmatic' "$OUTFILE"; then
    echo "             FAIL: search returned 200 but expected result was not rendered"
    record_fail "product-search-content"
    rm -f "$OUTFILE"
    return 1
  fi

  echo "             PASS: search result rendered"
  rm -f "$OUTFILE"
}


check_post_status() {
  local NAME="$1"
  local ENDPOINT_PATH="$2"
  local EXPECTED="$3"
  
  echo ""
  echo "[SECURITY] $NAME"
  echo "           POST $ENDPOINT_PATH"

  local CODE
  CODE=$(curl --silent --show-error --max-time 30 \
      --output /dev/null --write-out "%{http_code}" \
      -X POST -H "Content-Type: application/json" \
      -d '{"title":"validation-auth-test"}' \
      "$BASE_URL$ENDPOINT_PATH" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ]; then
    echo "           FAIL: curl exit code $RC"
    cat /tmp/validator_curl_error 2>/dev/null || true
    record_fail "$NAME"
    return 1
  fi

  echo "           HTTP $CODE (expected $EXPECTED)"
  if [ "$CODE" != "$EXPECTED" ]; then
    echo "           FAIL"
    record_fail "$NAME"
    return 1
  fi

  echo "           PASS"
}

check_redirect() {
  local NAME="$1"
  local ENDPOINT_PATH="$2"
  
  echo ""
  echo "[SECURITY] $NAME"
  echo "           $ENDPOINT_PATH"

  local HEADERS
  HEADERS=$(mktemp)
  local CODE
  CODE=$(curl --silent --show-error --max-time 30 \
      --output /dev/null --dump-header "$HEADERS" \
      --write-out "%{http_code}" "$BASE_URL$ENDPOINT_PATH" 2>/tmp/validator_curl_error)
  local RC=$?

  if [ "$RC" -ne 0 ] || [ "$CODE" != "302" ]; then
    echo "           FAIL: expected HTTP 302, got $CODE"
    record_fail "$NAME"
    rm -f "$HEADERS"
    return 1
  fi

  echo "           PASS: HTTP 302"
  rm -f "$HEADERS"
}

# -----------------------------------------------------------------------------
# 1. Infrastructure/application health
# -----------------------------------------------------------------------------
check_status "Root application" "/" "200" >/dev/null || true
check_status "Health endpoint" "/health" "200" >/dev/null || true
check_status "Functional health / DB-data gate" "/health/functional" "200" >/dev/null || true

# -----------------------------------------------------------------------------
# 2. Product functionality
# -----------------------------------------------------------------------------
FOUND_PRODUCT_ID=""

check_page_has_products "Product listing renders products" "/products/" || true

PRODUCT_ID="$FOUND_PRODUCT_ID"

if [ -n "$PRODUCT_ID" ]; then
  check_product_detail "$PRODUCT_ID" || true
fi

for CATEGORY in \
  electronics \
  fashion \
  books \
  home-kitchen \
  sports \
  toys \
  beauty \
  automotive; do
  check_category "$CATEGORY" || true
done

check_search || true

# Sorting/pagination must still render a real product, not just return 200.
check_page_has_products "Product sorting" "/products/?sort=name_desc" >/dev/null || true
check_page_has_products "Product pagination" "/products/?page=1" >/dev/null || true

# -----------------------------------------------------------------------------
# 3. Authentication / authorization behavior
# -----------------------------------------------------------------------------
check_status "Login page" "/auth/login" "200" >/dev/null || true
check_status "Registration page" "/auth/register" "200" >/dev/null || true
check_redirect "Cart requires authentication" "/cart/" || true
check_redirect "Orders requires authentication" "/orders/my-orders" || true

# ICM API must reject unauthenticated callers without creating data.
check_post_status "ICM API rejects unauthenticated request" "/admin/icm/api/incidents" "401" || true

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
echo ""
echo "============================================================"
echo "FUNCTIONAL VALIDATION SUMMARY"
echo "============================================================"

if [ "$FAILED" -eq 0 ]; then
  echo "RESULT: PASS"
  echo "All application, data, product, category, auth and ICM safety checks passed."
  if [ -n "${GITHUB_OUTPUT:-}" ]; then
    echo "failed_checks=" >> "$GITHUB_OUTPUT"
  fi
  exit 0
fi

echo "RESULT: FAIL"
echo "Failed checks:"
printf ' - %s\n' "${FAILED_CHECKS[@]}"

FAILED_CHECKS_CSV=$(IFS=,; echo "${FAILED_CHECKS[*]}")
if [ -n "${GITHUB_OUTPUT:-}" ]; then
  echo "failed_checks=$FAILED_CHECKS_CSV" >> "$GITHUB_OUTPUT"
fi

exit 1
