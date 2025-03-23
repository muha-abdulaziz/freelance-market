from flask import Blueprint
from .job_service import JobService
from flask import request

job_route = Blueprint('job', __name__, url_prefix='/job')

@job_route.post('/new/')
def create_new_job():
    job = JobService()
    return job.createNewJob(request.get_json()['title'])