from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
import datetime
from flask_sqlalchemy import SQLAlchemy

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

import Weather_API_Key #create Weather_API_Key with constant KEY = "api-key"  !gitignore
from  bot.botmain import startBot

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'HelloworldByeWorld'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('main.html')
    if request.method == "POST":
        return redirect('/places')


@app.route('/places', methods=["GET", "POST"])
def places():
    if request.method == "GET":
        return render_template('table.html')
    if request.method == "POST":
        return redirect('/places')


@app.route('/weatherHandler', methods=["POST"])
def weatherHandler():
    config = get_default_config()  # get_config_from("config.json")
    config['language'] = 'ru'
    owm = OWM(Weather_API_Key.KEY, config=config)
    mgr = owm.weather_manager()


if __name__ == "__main__":
    db.create_all()
    # startBot()
    app.run(port=5000)
