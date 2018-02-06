# Import from peewee
from peewee import *
from models import *
# Connect to the SQLite database

def create_tables():
    with db:
        db.create_tables([Event])

create_tables()

