from models import *

from playhouse.migrate import *
migrator = PostgresqlMigrator(db)
# Run the migration
# Peewee will throw an error if it doesn't work, but we can just use
# try/except to ignore it

city = CharField(default='')
state_code = CharField(default='',max_length=2)

try:  
    migrate(
        migrator.add_column('events', 'city', city),
        migrator.add_column('events', 'state_code', state_code),
    )
except:
  print "Already added columns, skipping!"
