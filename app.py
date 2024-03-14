from flask import Flask,session,request,jsonify
from controllers import user_blueprint,course_blueprint,user_course_blueprint
from models import db
import logging
from models.result_entity import ResultEntity
logging.basicConfig(level=logging.DEBUG)  # 设置日志级别为 DEBUG
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key'


app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(course_blueprint, url_prefix='/course')
app.register_blueprint(user_course_blueprint, url_prefix='/user_course')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}" \
    .format('root', 'jackyWU0225', '127.0.0.1:3306', '00000')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 事件系统跟踪修改
db.init_app(app)


if __name__ == '__main__':
    app.run()
