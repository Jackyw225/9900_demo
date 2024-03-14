from models import db

class CourseModel(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date1 = db.Column(db.String(255))
    t_id  = db.Column(db.Integer)
    date2 = db.Column(db.String(255))
    description = db.Column(db.String(255))