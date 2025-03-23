
class Job():
    __tablename__ = 'jobs'

    def __init__(self, title=None, description=None, timestamps=None):
        self.title = title
        self.description = description
        self.timestamps = timestamps

    def __repr__(self):
        return f'<Job {self.title!r}>'


def create():
    return "created"


def fetch():
    list = []
    return list
