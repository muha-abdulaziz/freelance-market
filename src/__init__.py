import os
from flask import Flask , render_template
# from .jobs.route import job_route
# from .db.database import init_db


def create_app(test_config=None):
    try:
        # init_db()
        app = Flask(__name__, instance_relative_config=True)
        # app.register_blueprint(job_route)

        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        @app.route('/')
        def home():
            return render_template('index.html', title="Home Page")

        @app.route('/hello')
        def hello():
            return 'Python Flask'

        return app
    except Exception as e:
        print("unable to start the server!")
        print(e)
