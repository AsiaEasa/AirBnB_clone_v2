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
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        IOS = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and kwargs != {}:
            for K, V in kwargs.items():
                if K == "created_at" or K == "updated_at":
                    self.__dict__[K] = datetime.strptime(V, IOS)
                else:
                    if K != "__class__":
                        setattr(self, K, V)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

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
