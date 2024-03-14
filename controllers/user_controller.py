from flask import jsonify, request,Blueprint
from models import db
from models.user_model import UserModel
from models.result_entity import ResultEntity
from . import user_blueprint
from interceptor import interceptor
from sqlalchemy import text
@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        result_entity = ResultEntity(code=500, msg='Username and password are required')
        return jsonify(result_entity.__dict__)

    user = UserModel.query.filter_by(email=username).first()

    # Check if the user exists and the password is correct
    if not user or user.password != password:
        result_entity = ResultEntity(code=500, msg='Invalid username or password')
        return jsonify(result_entity.__dict__)


    # Here you might generate and return a JWT token for the authenticated user
    result_entity = ResultEntity(code=200, msg='Login successful',data=user.id)
    return jsonify(result_entity.__dict__)

@user_blueprint.route('/findByStudentId/<int:c_id>', methods=['GET'])
@interceptor
def findByStudentId(c_id):
    custom_query = text("SELECT * FROM user WHERE id in (select student_id from user_course_realation where c_id=:c_id) ")

    # 使用 db.session.execute 执行自定义查询
    result = db.session.execute(custom_query, {"c_id": c_id})

    users_list = [{'id': user.id, 'name': user.name, 'email': user.email, 'type': user.type, 'address': user.address}
                  for user in result]

    result_entity = ResultEntity(code=200, msg='Success',data=users_list)
    return jsonify(result_entity.__dict__)

@user_blueprint.route('/listAll', methods=['GET'])
@interceptor
def listAll():
    all_users = UserModel.query.filter_by(type=1).all()
    users_list = [{'id': user.id, 'name': user.name, 'email': user.email, 'type': user.type, 'address': user.address}
                  for user in all_users]

    result_entity = ResultEntity(code=200, msg='Success',data=users_list)
    return jsonify(result_entity.__dict__)


@user_blueprint.route('/', methods=['POST'])
def create_user() :
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    user_type = data.get('type')
    address = data.get('address')
    create_user = add_user(name, email, password, user_type, address)
    if create_user:
        result_entity = ResultEntity(code=200, msg='Success')
    else:
        result_entity = ResultEntity(code=500, msg='Check the information')
    return jsonify(result_entity.__dict__)


def add_user(name, email, password, user_type, address=None):
    new_user = UserModel(name=name, email=email, password=password, type=user_type, address=address)
    db.session.add(new_user)
    try:
        db.session.commit()
    except:
        return False
    return True


@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@interceptor
def delete_user_by_id(user_id):
    # 根据用户ID查询用户
    user_to_delete = UserModel.query.get(user_id)

    if user_to_delete:
        # 删除用户
        db.session.delete(user_to_delete)
        db.session.commit()

        result_entity = ResultEntity(code=200, msg='Success')
        return jsonify(result_entity.__dict__)
    else:
        # 如果找不到用户，返回相应的错误信息
        result_entity = ResultEntity(code=500, msg='not exits')
        return jsonify(result_entity.__dict__)

@user_blueprint.route('/<int:user_id>', methods=['GET'])
@interceptor
def get_user(user_id):
    user = UserModel.query.get(user_id)
    if user:
        user_info = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'type': user.type,
            'password': user.password,
            'address': user.address,
            'experience':user.experience,
            'phone':user.phone
        }

        result_entity = ResultEntity(code=200, msg='Success',data=user_info)
        return jsonify(result_entity.__dict__)
    result_entity = ResultEntity(code=200, msg='not exits')
    return jsonify(result_entity.__dict__)

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    updated_user = update_user(user_id, name=data.get('name'), email=data.get('email'), password=data.get('password'), user_type=data.get('type'), address=data.get('address'), phone=data.get('phone'), experience=data.get('experience'))
    if updated_user:
        result_entity = ResultEntity(code=200, msg='Success')
        return jsonify(result_entity.__dict__)
    result_entity = ResultEntity(code=500, msg='not exits')
    return jsonify(result_entity.__dict__)


def update_user(user_id, name=None, email=None, password=None, user_type=None, address=None, phone=None, experience=None):
    user = UserModel.query.get(user_id)
    if user:
        user.name = name if name is not None else user.name
        user.email = email if email is not None else user.email
        user.password = password if password is not None else user.password
        user.type = user_type if user_type is not None else user.type
        user.address = address if address is not None else user.address
        user.phone = phone if phone is not None else user.phone
        user.experience = experience if experience is not None else user.experience
        db.session.commit()
        return user
    return None

@user_blueprint.route('/forget', methods=['POST'])
def forget():
    data = request.get_json()
    user_query = UserModel.query.filter(UserModel.address == data.get('address'), UserModel.email == data.get('email')).first()

    if user_query:
        updated_user = update_user(user_query.id,None, None,
                                   data.get('password'), None,
                                   None, None,
                                   None);
        if updated_user:
            result_entity = ResultEntity(code=200, msg='Success')
            return jsonify(result_entity.__dict__)

        result_entity = ResultEntity(code=500, msg='Eror',data=user_info)
        return jsonify(result_entity.__dict__)
    result_entity = ResultEntity(code=500, msg='not exits')
    return jsonify(result_entity.__dict__)