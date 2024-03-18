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

        @property
        def cities(self):
            """getter for the cities attribute
            * returns the list of City instances with state_id equals
            to the current State.id
            * It will be the FileStorage relationship between State and
            City
            """
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
