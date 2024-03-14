from models import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    experience = db.Column(db.String(255))