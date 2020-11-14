from flask import Flask, jsonify, render_template, request, redirect, url_for, session, \
    make_response, flash
import datetime
import threading
import Weather_API_Key  # create Weather_API_Key with constant KEY = "api-key"  !gitignore
from bot.botmain import startBot
import config
from weather_data import weather

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'HelloworldByeWorld'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('main.html')
    if request.method == "POST":
        #print(f'Search: {request.form["search"]}; Radius: {request.form["radius"]}')
        city = request.form["search"]
        radius = request.form["radius"]
        t = weather(city, radius)
        if t:
            for i in range(len(t)):
                t[i].append(i+1)
            #print(t)
            return render_template('table.html', place=t, main_city=request.form["search"])
        else:
            flash('Неверные данные')
            return render_template('main.html')


@app.route('/weatherHandler', methods=["POST"])
def weatherHandler():
    t = weather(request.form['city'], request.form['radius'])
    print('ok')
    if t==None:
        return jsonify(city=["Incorrect input"], temp=["-300"], weather=[''])
    else:
        t.sort(key=lambda p: p[1], reverse=True)
        cities = []
        temps = []
        weathers = []
        for i in range(len(t)):
            cities.append(t[i][0])
            temps.append(t[i][1])
            weathers.append(t[i][3])
        return jsonify(city=cities, temp=temps, weather=weathers)


def startServer():
    app.run(host=config.host, port=int(config.port))


if __name__ == "__main__":
    s = threading.Thread(target=startServer)
    s.start()
    startBot()
