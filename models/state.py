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
        """getter attribute cities"""
        cities_list = []
        for K, V in models.storage.all().items():
            NAME = key.replace('.', ' ')
            PART = shlex.split(NAME)
            if PART[0] == 'City' and V.state_id == self.id:
                cities_list.append(V)
        return cities_list
