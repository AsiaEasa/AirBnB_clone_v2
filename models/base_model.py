#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.created_at = datetime.strptime(kwargs.get(
                    'created_at', datetime.now().strftime(
                     '%Y-%m-%dT%H:%M:%S.%f')), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get(
                    'updated_at', datetime.now().strftime(
                     '%Y-%m-%dT%H:%M:%S.%f')), '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key not in ['created_at', 'updated_at']:
                    setattr(self, key, value)

    def __str__(self):
        """ To handle print()
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ UPDATE the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_C = self.__dict__.copy()
        K = ["created_at", "updated_at"]
        for KEY, V in self.__dict__.items():
            if KEY in K:
                dict_C[KEY] = V.isoformat()
        dict_C['__class__'] = self.__class__.__name__
        if "_sa_instance_state" in dict_C:
            del dict_C["_sa_instance_state"]
        return dict_C

    def delete(self):
        """ Deletes the current instance from the storage """
        models.storage.delete(self)
