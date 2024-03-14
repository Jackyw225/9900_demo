from flask import Blueprint

course_blueprint = Blueprint('course', __name__)
user_blueprint = Blueprint('user', __name__)
user_course_blueprint = Blueprint('user_course', __name__)
from .user_controller import *
from .course_controller import *
from .user_course_realation_controller import *