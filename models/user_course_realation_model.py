from models import db

class UserCourseRealation(db.Model):
    __tablename__ = 'user_course_realation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer)
    c_id = db.Column(db.String(255))