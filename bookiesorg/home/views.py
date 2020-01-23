'''This is a docstring for the views in my homepage'''
from flask import Flask, request, render_template, flash, redirect, make_response, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from home import app
from . import db

@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("bookiesorg.html")

@app.route("/aboutus")
def aboutus():
    return render_template("bookiesorgaboutus.html")

@app.route("/missionandvision")
def missionandvision():
    return render_template("bookiesmissionandvision.html")