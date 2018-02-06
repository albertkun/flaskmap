# Import from peewee
from peewee import *

# Connect to the SQLite database

db = PostgresqlDatabase('flaskmap', user='postgres', password='secret',
                           host='127.0.0.1', port=5432)
# Connect to our database.
db.connect()

# Define what a 'School' is
class Event(Model):
  # These are all the fields it has
  # match up CharField/IntegerField/etc with correct type
  uid = CharField(primary_key=True) # primary key = unique id
  event_name = CharField()
  neighborhood = CharField()
  address = CharField()
  city = CharField()
  state_code = CharField()
  zipcode = FixedCharField(max_length=5)
  date = DateTimeField()
  attendees = IntegerField()
  url = CharField()
  lat = DecimalField()
  lon = DecimalField()

  def full_address(self):
    return "{},{},{},{}".format(self.address,self.city,self.state_code,
                                self.zipcode)
  class Meta:
    # data is coming from schools.db
    database = db
    # and it's in the table called 'schools'
    db_table = 'events'


