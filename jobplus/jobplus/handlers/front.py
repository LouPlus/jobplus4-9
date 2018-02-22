from flask import Blueprint,render_template
from jobplus.models import db,User,Company,Job
from  jobplus.forms import ApplicantRegisterForm,LoginForm,CompanyRegisterForm

front = Blueprint('front',__name__)


@front.route('/')
def index():
    users = User.query.all()
    return render_template('index.html',users=users)

@front.route('/company_register')
def company_register():
    form=CompanyRegisterForm()
    return render_template('company_register.html',form=form)

@front.route('/applicant_register')
def applicant_register():
    form=ApplicantRegisterForm()
    return render_template('applicant_register.html',form=form)


@front.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',form=form)

