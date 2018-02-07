# Import from peewee
from peewee import *

# Connect to the PostgresqlDatabase

db = PostgresqlDatabase('flaskmap', user='postgres', password='secret',
                           host='127.0.0.1', port=5432)
# Connect to our database.
db.connect()

# Define what a 'Event' is
class Event(Model):
  # These are all the fields it has
  # match up CharField/IntegerField/etc with correct type
  uid = CharField(primary_key=True) # primary key = unique id
  event_name = CharField()
  neighborhood = CharField()
  address = CharField()
  city = CharField()
  state_code = CharField()
  zipcode = FixedCharField(null = True,max_length=5)
  date = DateTimeField()
  attendees = IntegerField()
  url = CharField()
  lat = DecimalField(null = True)
  lon = DecimalField(null = True)

  def full_address(self):
    return "{},{},{}".format(self.address,self.city,self.state_code)

  
  class Meta:
    # data is coming from schools.db
    database = db
    # and it's in the table called 'events'
    db_table = 'events'


