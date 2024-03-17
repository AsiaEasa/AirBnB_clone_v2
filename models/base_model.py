#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

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
        storage.delete(self)
