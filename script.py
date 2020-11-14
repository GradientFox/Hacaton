from flask import Flask, jsonify, render_template, request, redirect, url_for, session, \
    make_response, flash
import datetime
from flask_sqlalchemy import SQLAlchemy
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

import threading
import Weather_API_Key  # create Weather_API_Key with constant KEY = "api-key"  !gitignore
from bot.botmain import startBot
import config

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'HelloworldByeWorld'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/weatherHandler', methods=["POST"])
def weatherHandler():
    # config = get_default_config()  # get_config_from("config.json")
    # config['language'] = 'ru'
    # owm = OWM(Weather_API_Key.KEY, config=config)
    # mgr = owm.weather_manager()

    #Отладка
    print(request.form['city'])
    return jsonify(city=request.form['city'], temp="34", weather="good")


def startServer():
    app.run(host=config.host, port=int(config.port))


if __name__ == "__main__":
    s = threading.Thread(target=startServer)
    s.start()
    startBot()
