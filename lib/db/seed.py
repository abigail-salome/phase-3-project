from models import Destination, Review, User
from sqlalchemy.orm import sessionmaker
from models import engine

Session = sessionmaker(bind=engine)
session = Session()


def seed_data():
    # Add Users
    user1 = User(name="Alice Smith", email="alice@example.com")
    user2 = User(name="Bob Johnson", email="bob@example.com")
    session.add_all([user1, user2])

    # Add Destinations
    dest1 = Destination(
        name="Mount Kilimanjaro",
        description="The highest mountain in Africa",
        location="Tanzania",
    )
    dest2 = Destination(
        name="Victoria Falls",
        description="A magnificent waterfall",
        location="Zambia/Zimbabwe",
    )
    session.add_all([dest1, dest2])

    # Add Reviews
    review1 = Review(
        content="Amazing experience!", rating=5, destination=dest1, user=user1
    )
    review2 = Review(
        content="Breathtaking views!", rating=5, destination=dest2, user=user2
    )
    session.add_all([review1, review2])

    session.commit()


if __name__ == "__main__":
    seed_data()
