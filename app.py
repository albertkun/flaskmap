#from config import *
from flask import Flask, jsonify, render_template, request
import simplejson
from playhouse.shortcuts import model_to_dict, dict_to_model
from flask_marshmallow import Marshmallow

# define the app here
app = Flask(__name__)

# here is the marshmallow app definition for the api
ma = Marshmallow(app)

# bring in the table models
from models import *

### api schema begins here ###
class bookingSchema(ma.Schema):
    class Meta:
        # Fields to expose through api
        fields = ('fid', 'desc_', 'slug','sex','charge','age','home_addre','x','y')
        json_module = simplejson

booking_schema = bookingSchema()
bookings_schema = bookingSchema(many=True)

### api schema ends here ###

def basicQuery():
	global bookings
	global neighborhoods

	bookings = lapd.select()
    # neighborhoods = lapd.select(lapd.slug).distinct().order_by(lapd.slug.asc())
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

@app.route("/<slug>/bookings/", methods=['GET'])
def get_events(slug):
    all_bookings = lapd.select().where(lapd.slug == slug)
    result = bookings_schema.dump(all_bookings)
    return jsonify(result.data)


### not needed anymore ###
# @app.route('/_neighborhood')
# def neighborhood():
# 	slug = request.args.get('slug')
# 	# return slug
# 	bookings = lapd.select().where(lapd.slug == slug)
# 	# json_data = json.dumps(model_to_dict(bookings))
# 	# return json_data
# 	# return jsonify(model_to_dict(bookings))
# 	return BinaryJSONField({'rows':[model_to_dict(booking) for booking in bookings]})

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
