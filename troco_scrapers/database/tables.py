from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Text
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Home(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key = True)
    title = Column(String(255))
    owner_name = Column(String(255))
    link = Column(String(255), unique=True)
    description = Column(Text)
    sleeps = Column(Integer)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    property_type = Column(String(255))
    min_stay = Column(String(255))

class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))

class Amenities(Base):
    __tablename__ = 'amenities'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

class PropertyAmenities(Base):
    __tablename__ = 'property_amenity'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    amenity_id = Column(Integer, ForeignKey('amenities.id'))
    description = Column(String(255))

class Suitability(Base):
    __tablename__ = 'suitabilities'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

class PropertySuitability(Base):
    __tablename__ = 'property_suitability'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    suitability_id = Column(Integer, ForeignKey('amenities.id'))

class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

class PropertyLocations(Base):
    __tablename__ = 'property_location'
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))

class DroppedItems(Base):
    __tablename__ = 'dropped_items'
    id = Column(Integer, primary_key=True)
    reason = Column(String(45))
    data = Column(Text)
    link = Column(String(100))


engine = create_engine('mysql://dev:Pa$sw0rd@localhost/homeaway')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
