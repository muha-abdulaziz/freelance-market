from flask import Blueprint, jsonify, request
from src.services.jobs import JobService

jobs_bp = Blueprint("job", __name__, url_prefix="/job")


@jobs_bp.post("/")
def create_new_job():
    data = request.json

    if not data:
        return jsonify({"error": "Missing data"}), 400
    if "title" not in data:
        return jsonify({"error": "Missing title"}), 400
    if "description" not in data:
        return jsonify({"error": "Missing description"}), 400

    job = JobService.create_job(data["title"], data["description"])
    return jsonify(job.to_dict()), 201
