import hmac

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
    current_app,
)

from ecommerce.decorators.admin import admin_required
from ecommerce.extensions import db
from ecommerce.models.incident import Incident

icm_bp = Blueprint("icm", __name__, url_prefix="/admin/icm")


SEVERITIES = ["Low", "Medium", "High", "Critical"]
STATUSES = ["Open", "Investigating", "RCA Confirmed", "Remediation Pending", "Resolved"]


def _next_incident_number():
    latest = Incident.query.order_by(Incident.id.desc()).first()
    next_id = (latest.id + 1) if latest else 1
    return f"ICM-{next_id:06d}"

def _api_token_required():
    expected_token = current_app.config.get("ICM_API_TOKEN")

    if not expected_token:
        return jsonify({
            "error": "ICM API token is not configured."
        }), 500

    auth_header = request.headers.get("Authorization", "")
    expected_header = f"Bearer {expected_token}"

    if not hmac.compare_digest(auth_header, expected_header):
        return jsonify({
            "error": "Unauthorized."
        }), 401

    return None

@icm_bp.route("/api/incidents", methods=["POST"])
def create_api_incident():

    auth_error = _api_token_required()

    if auth_error:
        return auth_error

    data = request.get_json(silent=True) or {}

    title = data.get("title", "").strip()

    if not title:
        return jsonify({
            "error": "Incident title is required."
        }), 400

    incident = Incident(
        incident_number=_next_incident_number(),
        title=title,
        severity=data.get("severity", "Medium"),
        status=data.get("status", "Open"),
        application=data.get("application", "ecommercelab-app").strip(),
        environment=data.get("environment", "Production").strip(),
        pipeline_name=data.get("pipeline_name"),
        pipeline_run_id=data.get("pipeline_run_id"),
        commit_sha=data.get("commit_sha"),
        candidate_revision=data.get("candidate_revision"),
        previous_revision=data.get("previous_revision"),
        failed_endpoints=data.get("failed_endpoints"),
        failure_summary=data.get("failure_summary"),
    )

    if incident.severity not in SEVERITIES:
        incident.severity = "Medium"

    if incident.status not in STATUSES:
        incident.status = "Open"

    db.session.add(incident)
    db.session.commit()

    return jsonify({
        "message": "Incident created successfully.",
        "incident_id": incident.id,
        "incident_number": incident.incident_number,
        "status": incident.status
    }), 201

@icm_bp.route("/api/incidents/<int:incident_id>", methods=["GET"])
def get_api_incident(incident_id):
    auth_error = _api_token_required()

    if auth_error:
        return auth_error

    incident = Incident.query.get(incident_id)

    if incident is None:
        return jsonify({
            "error": "Incident not found."
        }), 404

    return jsonify({
        "incident_id": incident.id,
        "incident_number": incident.incident_number,
        "title": incident.title,
        "severity": incident.severity,
        "status": incident.status,
        "application": incident.application,
        "environment": incident.environment,
        "pipeline_name": incident.pipeline_name,
        "pipeline_run_id": incident.pipeline_run_id,
        "commit_sha": incident.commit_sha,
        "candidate_revision": incident.candidate_revision,
        "previous_revision": incident.previous_revision,
        "failed_endpoints": incident.failed_endpoints,
        "failure_summary": incident.failure_summary,
        "rca_summary": incident.rca_summary,
        "recommended_action": incident.recommended_action,
        "created_at": (
            incident.created_at.isoformat()
            if incident.created_at
            else None
        ),
        "updated_at": (
            incident.updated_at.isoformat()
            if getattr(incident, "updated_at", None)
            else None
        ),
    }), 200

@icm_bp.route("/api/incidents/<int:incident_id>", methods=["PATCH"])
def update_api_incident(incident_id):
    """
    Machine-to-machine ICM update endpoint.

    Used by trusted automation such as the GitHub Actions deployment
    pipeline after SRE analysis has completed.

    Authentication uses the same ICM API bearer token as incident creation.
    """

    auth_error = _api_token_required()

    if auth_error:
        return auth_error

    incident = Incident.query.get_or_404(incident_id)

    data = request.get_json(silent=True) or {}

    if "status" in data:
        status = data["status"]

        if status not in STATUSES:
            return jsonify({
                "error": f"Invalid status: {status}"
            }), 400

        incident.status = status

    if "severity" in data:
        severity = data["severity"]

        if severity not in SEVERITIES:
            return jsonify({
                "error": f"Invalid severity: {severity}"
            }), 400

        incident.severity = severity

    if "rca_summary" in data:
        incident.rca_summary = (
            str(data["rca_summary"]).strip() or None
        )

    if "recommended_action" in data:
        incident.recommended_action = (
            str(data["recommended_action"]).strip() or None
        )

    db.session.commit()

    return jsonify({
        "message": "Incident updated successfully.",
        "incident_id": incident.id,
        "incident_number": incident.incident_number,
        "status": incident.status,
        "severity": incident.severity,
    }), 200

@icm_bp.route("/")
@admin_required
def index():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return render_template("admin/icm/index.html", incidents=incidents)


@icm_bp.route("/create", methods=["GET", "POST"])
@admin_required
def create():
    if request.method == "POST":
        incident = Incident(
            incident_number=_next_incident_number(),
            title=request.form.get("title", "").strip(),
            severity=request.form.get("severity", "Medium"),
            status=request.form.get("status", "Open"),
            application=request.form.get("application", "ecommercelab-app").strip(),
            environment=request.form.get("environment", "Production").strip(),
            pipeline_name=request.form.get("pipeline_name", "").strip() or None,
            pipeline_run_id=request.form.get("pipeline_run_id", "").strip() or None,
            commit_sha=request.form.get("commit_sha", "").strip() or None,
            candidate_revision=request.form.get("candidate_revision", "").strip() or None,
            previous_revision=request.form.get("previous_revision", "").strip() or None,
            failed_endpoints=request.form.get("failed_endpoints", "").strip() or None,
            failure_summary=request.form.get("failure_summary", "").strip() or None,
        )

        if not incident.title:
            flash("Incident title is required.", "danger")
            return render_template("admin/icm/create.html", incident=incident, severities=SEVERITIES, statuses=STATUSES)

        if incident.severity not in SEVERITIES:
            incident.severity = "Medium"
        if incident.status not in STATUSES:
            incident.status = "Open"

        db.session.add(incident)
        db.session.commit()
        flash(f"{incident.incident_number} created successfully.", "success")
        return redirect(url_for("icm.detail", incident_id=incident.id))

    return render_template("admin/icm/create.html", incident=None, severities=SEVERITIES, statuses=STATUSES)


@icm_bp.route("/<int:incident_id>")
@admin_required
def detail(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    return render_template("admin/icm/detail.html", incident=incident, statuses=STATUSES, severities=SEVERITIES)


@icm_bp.route("/<int:incident_id>/update", methods=["POST"])
@admin_required
def update(incident_id):
    incident = Incident.query.get_or_404(incident_id)

    incident.status = request.form.get("status", incident.status)
    incident.severity = request.form.get("severity", incident.severity)
    incident.rca_summary = request.form.get("rca_summary", "").strip() or None
    incident.recommended_action = request.form.get("recommended_action", "").strip() or None

    if incident.status not in STATUSES:
        incident.status = "Open"
    if incident.severity not in SEVERITIES:
        incident.severity = "Medium"

    db.session.commit()
    flash(f"{incident.incident_number} updated successfully.", "success")
    return redirect(url_for("icm.detail", incident_id=incident.id))
