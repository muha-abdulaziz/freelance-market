from src.models.job import Job
from src.repositories.jobs import JobsRepository


class JobService:
    @staticmethod
    def create_job(title: str, description: str) -> Job:
        return JobsRepository.create_job(title, description)
