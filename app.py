#from config import *
from flask import Flask, render_template
from models import *

app = Flask(__name__)

@app.route('/')
def index():
  count = Event.select().count
  events = Event.select().order_by(Event.date.asc())
  return render_template('index.html',events=events)

@app.route('/events/<uid>')
def uid(uid=None):
    events = Event.select().where(Event.uid == uid)
    #return render_template('event.html', events=events)
    return render_template('map.html', events=events)  

if __name__ == '__main__':
    app.run(debug=True)
