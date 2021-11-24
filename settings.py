# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# creating an instance of the flask app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure our Database
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'u139539474_movie')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
