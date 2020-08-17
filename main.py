import feedparser
from flask import Flask
from flask import render_template
from flask import request

import api_requests

import json
import urllib
import datetime
from flask import make_response  #cookies
import keys

CURRENCY_URL = 'https://data.fixer.io/api/latest'


app = Flask(__name__)
DEFAULTS = {'publication': 'hnn',
            'city': 'Jerusalem',
            'base_currency':'USD'}



RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'hnn':'https://hnrss.org/newest'}

api_key = 'cc54e7ba3acbe5b0ea3337eed2102f8d'

def get_weather(city):
    api_url =  f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    request_response = urllib.request.urlopen(api_url)
    # print('Request URL: \n', request_response.get)
    print('Request info \n', request_response.info())
    print('Header Information: \n', request_response.getheaders())
    data = request_response.read()
    parsed = json.loads(data)
    print('Printing response: \n', parsed)
    main_weather = None
    if parsed.get('main'):
        temp_c = float(parsed['main']['temp']) - 273
        main_weather = {'city': parsed["name"], 'temp': temp_c}
        print('Weather Info', main_weather)
    return main_weather

def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication]) #feedparser object handles the request
    return feed



@app.route("/")
# @app.route("/<publication>")
#def get_news(publication='bbc'):
def home():
    """ This method uses flask requests
    request.args contains the GET arguments automatically
    .get() will check to see if your key was used and returns None if not used
    """
    publication = request.args.get("publication") 
    if not publication:
        publication = request.cookies.get('publication')
        if not publication:
            publication = DEFAULTS['publication']
    feed = get_news(publication)

    #get weather based on customer or DEFAULTS
    city = request.args.get("city")
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    temp = float(weather['temp'])
    weather['temp'] = '{:.2f}'.format(temp)
    print('city:', weather['city'])

    currency_info = api_requests.get_currency(CURRENCY_URL,'USD')
    base = currency_info['base']
    currency = 'ZAR'
    dollar_zar = float(currency_info['rates'][currency])
    rate = {'base':base, 'currency': currency, 'rate': '{:.2f}'.format(dollar_zar)}
    return render_template("home.html", articles=feed['entries'], weather=weather, rate=rate)

    # THE COOKIES - setting them
    response = make_response(render_template('home.html',
    articles=articles,
    weather=weather,
    currency_from=currency_from,
    currency_to=currency_to,
    rate=rate,
    currencies=sorted(currencies)))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie('publication',publication, expires=expires)
    response.set_cookie('city',city,expires=expires)
    # response.set_cookie('currency_to', currency_to, expires=expires)
    return response

   





if __name__ == "__main__":
  app.run(port=5000, debug=True)