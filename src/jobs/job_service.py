from . import create

class JobService:
    def createNewJob(self, title):
        create(create=title)
        return {"message": "Job has been created successfully"}
