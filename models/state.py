#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    def cities(self):
        ''' Retrieve all objects from storage'''
        objects = models.storage.all()
        cities_list = []
        for key, obj in objects.items():
            city_name = key.replace('.', ' ')
            city_parts = shlex.split(city_name)
            if city_parts[0] == 'City' and obj.state_id == self.id:
                cities_list.append(obj)
        return cities_list
