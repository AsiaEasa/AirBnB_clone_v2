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
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """ Deletes the current instance from the storage """
        models.storage.delete(self)
