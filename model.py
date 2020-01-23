from . import db
from datetime import datetime

class Users(db.Model):
    '''This models the users'''
    __tablename__ = "users"
    user_id= db.Column(db.Integer(),primary_key=True)
    full_name= db.Column(db.String(45),nullable=False)
    gender= db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(45),nullable=False)
    phone_no=db.Column(db.String(15),nullable=False)
    user_type_id=db.Column(db.Integer(),db.ForeignKey("user_type_id"))

class User_Type(db.model):
    '''This models the user types'''
    __tablename__ ="user_type"
    user_type_id= db.Column(db.Integer(),primary_key=True)
    usertype_name= db.Column(db.String(45),nullable=False)

'''This is for class referral classwork'''
class User(db.Model):
    '''This models the user'''
    __tablename__="user"
    id = db.Column(db.Integer(),primary_key=True)
    fullname= db.Column(db.String(100))
    email = db.Column(db.String(50))
    registration_date=db.Column(db.DateTime(),default=datetime.utcnow)
    
class Gift(db.Model):
    '''This models the gifts'''
    __tablename__="gift"
    id= db.Column(db.Integer(),primary_key=True)
    gift_name= db.Column(db.String(60))

class Guestgift(db.Model):
    guest_id
    

