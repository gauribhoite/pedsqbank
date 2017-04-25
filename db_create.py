from app import db
from models import *

# create the database and the db table
db.create_all()

# insert data
db.session.add(Question("A 56 year old male with liver disease and poor nutrition develops alopecia", 1,"Zinc deficiency leads to the above symptoms.","Multiple Choice",2))
# db.session.add(Question("Well", "I\'m well.","2003-08-04 12:30:45"))
# db.session.add(Question("Excellent", "I\'m excellent.","2003-08-04 12:30:45"))
# db.session.add(Question("Okay", "I\'m okay.","2003-08-04 12:30:45"))

# commit the changes
db.session.commit()
# "question": "I 1980 definerte helsepsykologen Matarazzo helsepsykologi som:",
# "answers": [
#     "”Læren om psykologiens innvirkning på helse”",
#     "”Psykologiens forhold til helse og utvikling av helseressurser”",
#     "”Det samlede bidra psykologien gir for å forstå helse og velvære ”",
#     "”Psykiske problemers innvirkning på helse”"
# ],
# "correct": 2