from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db,User,Company,Job
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

def register_blueprints(app):
    from .handlers import front, job, company, applicant, admin
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(applicant)
    app.register_blueprint(admin)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app,db)
    Bootstrap(app)

    register_blueprints(app)

    return app

