from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
import datetime
from flask_sqlalchemy import SQLAlchemy

from  bot.botmain import startBot

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'HelloworldByeWorld'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()
    startBot()
    app.run(port=5000)