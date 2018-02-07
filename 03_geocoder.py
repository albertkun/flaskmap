import requests
from time import sleep
from models import *

for event in Event.select().where(Event.lat.is_null()):
    print event
    try:
        # Form the URL with the address in it
        url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}".format(event.full_address())

        # Request the URL
        response = requests.get(url)

        # Traverse the Google API JSON to find location geometry array
        coords = response.json()['results'][0]['geometry']['location']

        # Assign the lat/lng into the object (the row)
        event.lat = coords['lat']
        event.lon = coords['lng']

        # And now save it to the database
        event.save()
        print "{} is at {}, {}".format(event.event_name, event.lat, event.lon)
        sleep(2)
    except:
      print "Failed to query/save for {}".format(event.event_name)
