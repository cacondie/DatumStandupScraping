from flask import Flask, render_template
from src.NationalDay import NationalDay
from src.ThisHistory import ThisDayInHistory
from src.Http import Http
import threading, webbrowser,random

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.debug=True

    return app
def get_data():
    http = Http()
    history = ThisDayInHistory(http)
    articles = history.get_articles()
    national_day = NationalDay(http)
    national_day.get_days()
    return articles, national_day


app = create_app()
@app.route('/')
def home_page():
    articles,national_day = get_data()
    return render_template("ThisDayHistory.html", articles=articles, national_day=national_day)

if __name__=="__main__":
    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    app.run(port=port, debug=False)