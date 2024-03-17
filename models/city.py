#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from models import ST

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if ST == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ''
        state_id = ''
