from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users' 
  # id (int), username (text), password (text), role (text)
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80), nullable=False, unique=True)
  name = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)
