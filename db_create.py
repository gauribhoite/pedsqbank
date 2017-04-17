from app import db
from models import *

# create the database and the db table
db.create_all()

# insert data
db.session.add(Question("Good", "I\'m good.","2003-08-04 12:30:45"))
db.session.add(Question("Well", "I\'m well.","2003-08-04 12:30:45"))
db.session.add(Question("Excellent", "I\'m excellent.","2003-08-04 12:30:45"))
db.session.add(Question("Okay", "I\'m okay.","2003-08-04 12:30:45"))

# commit the changes
db.session.commit()