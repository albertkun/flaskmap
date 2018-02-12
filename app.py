#from config import *
from flask import Flask, jsonify, render_template, request
from playhouse.shortcuts import model_to_dict, dict_to_model
app = Flask(__name__)


# from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

def basicQuery():
	global bookings
	global neighborhoods

	bookings = lapd.select()
	neighborhoods = lapd.select(lapd.slug).distinct().order_by(lapd.slug.asc())
	# bookings = lapd.select().where(lapd.slug == "downtown")

@app.route('/')
def index():
	basicQuery()
	bookings = lapd.select().where(lapd.slug == "downtown")
	count = lapd.select().where(lapd.slug == "downtown").count()
	return render_template('index.html',bookings=bookings,count=count,neighborhoods = neighborhoods)

# @app.route('/<slug>')
# def slug(slug=None):
# 	basicQuery()
# 	bookings = lapd.select().where(lapd.slug == slug)
# 	count = lapd.select().where(lapd.slug == slug).count()
# 	return render_template('index.html',bookings=bookings,count=count,neighborhoods = neighborhoods)

@app.route('/_neighborhood')
def neighborhood():
	slug = request.args.get('slug')
	# return slug
	bookings = lapd.select().where(lapd.slug == slug)
	# json_data = json.dumps(model_to_dict(bookings))
	# return json_data
	# return jsonify(model_to_dict(bookings))
	return BinaryJSONField({'rows':[model_to_dict(booking) for booking in bookings]})

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

# @app.route('/info')
# def info():
#   basicQuery()
#   return render_template('info.html', events=events)  

if __name__ == '__main__':
    app.run(debug=True)
