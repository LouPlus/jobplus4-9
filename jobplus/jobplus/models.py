from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for



db = SQLAlchemy()

class Base(db.Model):
    __abstract__=True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)


class UserToJob(Base):
    __tablename__ = 'user_to_job'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
	

class User(Base,UserMixin):
    __tablename__='user'

    ROLE_APPLICANT = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True,index=True,nullable=False)
    email = db.Column(db.String(64),unique=True, index=True, nullable=False)
    _password=db.Column('password',db.String(256),nullable=False)
    phone=db.Column(db.String(64))
    birthday=db.Column(db.DateTime)
    role = db.Column(db.SmallInteger)
    gender = db.Column(db.SmallInteger)
    resume_url = db.Column(db.String(256))
    company_id=db.Column(db.Integer,db.ForeignKey('company.id'))
    company=db.relationship('Company')
    applied_jobs =db.relationship('Job',secondary='user_to_job',backref='user')

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self,password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role==self.ROLE_COMPANY
		
    @property
    def is_applicant(self):
        return self.role==self.ROLE_APPLICANT		
		
		
		
class Job(Base):
    __tablename__='job'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique=True,index=True,nullable=False)
    salary_bottom=db.Column(db.Integer)
    salary_top=db.Column(db.Integer)
    experience=db.Column(db.String(256))
    location=db.Column(db.String(128))
    description = db.Column(db.String(256))
    requirement = db.Column(db.String(256))
    image_url=db.Column(db.String(256))
    company_id=db.Column(db.Integer,db.ForeignKey('company.id'))
    company=db.relationship('Company')
	

    
class Company(Base):
    __tablename__='company'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique=True,index=True,nullable=False)
    logo_url=db.Column(db.String(256))
    website=db.Column(db.String(256))
    location=db.Column(db.String(64))
    brief_description= db.Column(db.String(64))
    detailed_description = db.Column(db.String(256))
    published_jobs=db.relationship('Job')

    
    
    
