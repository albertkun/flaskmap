import requests
from time import sleep
from models import *

for event in Event.select().where(Event.lat <>''):
    print event
    sleep(1)
    try:
        # Form the URL with the address in it
        url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}".format(event.full_address())

        # Request the URL
        response = requests.get(url)

        # Dig deep into the JSON 
        # this will give us something like
        # {u'lat': 40.7135296, u'lng': -73.9856844}
        coords = response.json()['results'][0]['geometry']['location']

        # Assign the lat/lng into the object (the row)
        event.lat = coords['lat']
        event.lon = coords['lng']

        # And now save it to the database
        event.save()
        print "{} is at {}, {}".format(event.event_name, event.lat, event.lon)
    except:
      print "Failed to query/save for {}".format(event.event_name)
