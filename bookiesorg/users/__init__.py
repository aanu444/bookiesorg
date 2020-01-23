'''This is the docstring for users init'''
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import TestEnvironment




app= Flask(__name__, instance_relative_config=True)

csrf= CSRFProtect(app)

app.config.from_object(TestEnvironment)
app.config.from_pyfile('config.py',silent=True)

db: SQLAlchemy(app)
from bookiesorg.users import views