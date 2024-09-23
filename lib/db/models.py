from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    location = Column(String)
    reviews = relationship("Review", back_populates="destination")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    reviews = relationship("Review", back_populates="user")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    destination = relationship("Destination", back_populates="reviews")
    user = relationship("User", back_populates="reviews")


# Create the SQLite database
engine = create_engine("sqlite:///travel_guide.db")
Base.metadata.create_all(engine)
