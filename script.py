from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'HelloworldByeWorld'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)