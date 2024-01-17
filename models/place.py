#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Float, ForeignKey
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False, backref='place_amenities'
        )
    else:
        @property
        def review(self):
            rv_list = []
            reviews = models.strage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    rv_list.append(review)
            return rv_list

        @property
        def amenities(self):
            """ getter of amenities """
            am_list = []
            amenities = models.storage.all(Amenity)
            for key, objct in amenities.items():
                if key in self.amentiy_ids:
                    am_list.append(objct)
            return am_list

        @amenities.setter
        def amenities(self, obj=None):
            """Setter of amenity_ids"""
            if type(obj).__name__ == 'Amenity':
                num_amenity = 'Amenity' + '.' + obj.id
                self.amenity_ids.append(num_amenity)
