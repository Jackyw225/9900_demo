from flask import jsonify, request, Blueprint
from models import db
from models.user_course_realation_model import UserCourseRealation
from models.result_entity import ResultEntity
from . import user_course_blueprint
from interceptor import interceptor
from sqlalchemy import text

@user_course_blueprint.route('/', methods=['POST'])
@interceptor
def enroll_user_to_course():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('c_id')

    custom_delete_query = text("DELETE FROM user_course_realation WHERE c_id=:c_id and student_id=:student_id")
    db.session.execute(custom_delete_query, {"student_id": student_id, "c_id": course_id})
    db.session.commit()

    user_course_relation = UserCourseRealation(student_id=student_id, c_id=course_id)
    db.session.add(user_course_relation)
    db.session.commit()

    result_entity = ResultEntity(code=200, msg='Enrollment successful')
    return jsonify(result_entity.__dict__)


@user_course_blueprint.route('/<int:student_id>', methods=['GET'])
@interceptor
def get_user_courses(student_id):
    user_courses = UserCourseRealation.query.filter_by(student_id=student_id).all()

    courses_list = [{'id': relation.id, 'student_id': relation.student_id, 'c_id': relation.c_id}
                    for relation in user_courses]

    result_entity = ResultEntity(code=200, msg='Success', data=courses_list)
    return jsonify(result_entity.__dict__)


@user_course_blueprint.route('/t/<int:c_id>', methods=['GET'])
@interceptor
def t(c_id):
    user_courses = UserCourseRealation.query.filter_by(c_id=c_id).all()

    courses_list = [{'id': relation.id, 'student_id': relation.student_id, 'c_id': relation.c_id}
                    for relation in user_courses]

    result_entity = ResultEntity(code=200, msg='Success', data=courses_list)
    return jsonify(result_entity.__dict__)



@user_course_blueprint.route('/<int:relation_id>', methods=['DELETE'])
@interceptor
def remove_course_enrollment(relation_id):
    param1_value = request.args.get('c_id')
    custom_delete_query = text("DELETE FROM user_course_realation WHERE c_id=:c_id and student_id=:student_id")
    db.session.execute(custom_delete_query, {"student_id": relation_id,"c_id":param1_value})
    db.session.commit()
    result_entity = ResultEntity(code=200, msg='Deletion successful')
    return jsonify(result_entity.__dict__)


@user_course_blueprint.route('/<int:relation_id>', methods=['PUT'])
@interceptor
def update_course_enrollment(relation_id):
    data = request.get_json()
    updated_relation = update_user_course_relation(relation_id, student_id=data.get('student_id'),
                                                   course_id=data.get('course_id'))

    if updated_relation:
        result_entity = ResultEntity(code=200, msg='Update successful')
        return jsonify(result_entity.__dict__)
    else:
        result_entity = ResultEntity(code=500, msg='Relation not found')
        return jsonify(result_entity.__dict__)


def update_user_course_relation(relation_id, student_id=None, course_id=None):
    relation = UserCourseRealation.query.get(relation_id)

    if relation:
        relation.student_id = student_id if student_id is not None else relation.student_id
        relation.c_id = course_id if course_id is not None else relation.c_id
        db.session.commit()
        return relation

    return None