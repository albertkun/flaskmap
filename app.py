#from config import *
from flask import Flask, render_template
from models import *

app = Flask(__name__)
def basicQuery():
  global events
  events = Event.select().order_by(Event.date.asc())
  
  
@app.route('/')
def index():
  basicQuery()
  return render_template('index.html',events=events)

@app.route('/events/<uid>')
def uid(uid=None):
    events = Event.select().where(Event.uid == uid)
    return render_template('event.html', events=events)  

@app.route('/info')
def info():
  basicQuery()
  return render_template('info.html', events=events)  

if __name__ == '__main__':
    app.run(debug=True)
