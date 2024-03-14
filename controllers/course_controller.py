from flask import jsonify, request,Blueprint
from models import db
from models.course_model import CourseModel
from models.result_entity import ResultEntity
from . import course_blueprint
from interceptor import interceptor
from flask import Flask, request
from sqlalchemy import text

@course_blueprint.route('/listAll', methods=['GET'])
@interceptor
def listAll():
    param1_value = request.args.get('t_id')

    all_users = CourseModel.query.filter_by(t_id=param1_value).order_by(CourseModel.date1,CourseModel.date2).all()
    users_list = [{'id': course.id,
            'name': course.name,
            'date1': course.date1,
            'date2': course.date2,
            'description': course.description}
                  for course in all_users]

    result_entity = ResultEntity(code=200, msg='Success',data=users_list)
    return jsonify(result_entity.__dict__)

@course_blueprint.route('/findByStudentId/<int:student_id>', methods=['GET'])
@interceptor
def findByStudentId(student_id):
    custom_query = text("SELECT * FROM course WHERE id in (select c_id from user_course_realation where student_id=:student_id)")

    # 使用 db.session.execute 执行自定义查询
    result = db.session.execute(custom_query, {"student_id": student_id})

    users_list = [{'id': course.id,
            'name': course.name,
            'date1': course.date1,
            'date2': course.date2,
            'description': course.description}
                  for course in result]

    result_entity = ResultEntity(code=200, msg='Success',data=users_list)
    return jsonify(result_entity.__dict__)



@course_blueprint.route('/', methods=['POST'])
@interceptor
def create_user():
    data = request.get_json()
    new_course = CourseModel(
        name=data.get('name'),
        date1=data.get('date1'),
        date2=data.get('date2'),
        description=data.get('description'),
        t_id=data.get('t_id'),
    )
    db.session.add(new_course)
    try:
        db.session.commit()
        result_entity = ResultEntity(code=200, msg='Success')
    except:
        result_entity = ResultEntity(code=500, msg='Check Course name')
    return jsonify(result_entity.__dict__)



#


@course_blueprint.route('/<int:course_id>', methods=['DELETE'])
@interceptor
def delete_user_by_id(course_id):
    # 根据用户ID查询用户
    course_to_delete = CourseModel.query.get(course_id)

    if course_to_delete:
        # 删除用户
        db.session.delete(course_to_delete)
        db.session.commit()

        result_entity = ResultEntity(code=200, msg='Success')
        return jsonify(result_entity.__dict__)
    else:
        # 如果找不到用户，返回相应的错误信息
        result_entity = ResultEntity(code=500, msg='not exits')
        return jsonify(result_entity.__dict__)

@course_blueprint.route('/<int:course_id>', methods=['GET'])
@interceptor
def get_user(course_id):
    course = CourseModel.query.get(course_id)
    if course:
        course_info = {
            'id': course.id,
            'name': course.name,
            'date1': course.date1,
            'date2': course.date2,
            'description': course.description
        }

        result_entity = ResultEntity(code=200, msg='Success',data=course_info)
        return jsonify(result_entity.__dict__)
    result_entity = ResultEntity(code=200, msg='not exits')
    return jsonify(result_entity.__dict__)

@course_blueprint.route('/<int:course_id>', methods=['PUT'])
@interceptor
def update_user_route(course_id):
    course = CourseModel.query.get(course_id)
    if course:
        data = request.json
        course.name = data.get('name')
        course.date1 = data.get('date1')
        course.date2 = data.get('date2')
        course.description = data.get('description')
        db.session.commit()
        result_entity = ResultEntity(code=200, msg='Success')
        return jsonify(result_entity.__dict__)
    result_entity = ResultEntity(code=500, msg='not exits')
    return jsonify(result_entity.__dict__)


