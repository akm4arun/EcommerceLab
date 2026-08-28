from datetime import datetime, timezone

from ecommerce.extensions import db


class Incident(db.Model):
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    incident_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    severity = db.Column(db.String(20), nullable=False, default="Medium")
    status = db.Column(db.String(30), nullable=False, default="Open")
    application = db.Column(db.String(100), nullable=False, default="ecommercelab-app")
    environment = db.Column(db.String(50), nullable=False, default="Production")
    pipeline_name = db.Column(db.String(200), nullable=True)
    pipeline_run_id = db.Column(db.String(100), nullable=True)
    commit_sha = db.Column(db.String(64), nullable=True)
    candidate_revision = db.Column(db.String(150), nullable=True)
    previous_revision = db.Column(db.String(150), nullable=True)
    failed_endpoints = db.Column(db.Text, nullable=True)
    failure_summary = db.Column(db.Text, nullable=True)
    rca_summary = db.Column(db.Text, nullable=True)
    recommended_action = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self):
        return f"<Incident {self.incident_number}>"
