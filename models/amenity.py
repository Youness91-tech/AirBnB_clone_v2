#!/usr/bin/python3
""" the amenity class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Amenity Model """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
