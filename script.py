from flask import Flask, jsonify, render_template, request, redirect, url_for, session, \
    make_response, flash
import datetime
from flask_sqlalchemy import SQLAlchemy
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from weather_data import weather
import threading
import Weather_API_Key  # create Weather_API_Key with constant KEY = "api-key"  !gitignore
# from bot.botmain import startBot
import config

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
        print(f'Search: {request.form["search"]}; Radius: {request.form["radius"]}')
        city = request.form["search"]
        radius = request.form["radius"]
        t = weather(city, radius)
        if t:
            for i in range(len(t)):
                t[i].append(i+1)
            print(t)
            return render_template('table.html', place=t, main_city=request.form["search"])
        else:
            flash('Неверные данные')
            return render_template('main.html')


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
    app.run()
    # s = threading.Thread(target=startServer)
    # s.start()
    # startBot()
