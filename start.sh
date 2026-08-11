#!/bin/sh
set -e

echo "Running database migrations..."
flask db upgrade

echo "Starting application..."

# If gunicorn exists (Linux/container), use it.
if command -v gunicorn >/dev/null 2>&1; then
    exec gunicorn app:app --bind 0.0.0.0:8000
else
    # Windows/local fallback
    exec flask run --host=0.0.0.0 --port=8000
fi