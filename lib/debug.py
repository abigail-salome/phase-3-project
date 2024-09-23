from sqlalchemy.orm import sessionmaker
from db.models import Destination, engine

Session = sessionmaker(bind=engine)
session = Session()


destinations = session.query(Destination).all()
for destination in destinations:
    print(destination)
