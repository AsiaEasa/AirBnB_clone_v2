#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """ Class BaseModel
    """

    "The INIT method"
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # <-- Ensure storage.new() is called correctly
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            else:
                if isinstance(kwargs['created_at'], str):
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')

            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            else:
                if isinstance(kwargs['updated_at'], str):
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')

            del kwargs['__class__']

            self.__dict__.update(kwargs)

    def save(self):
        """ UPDATE the public instance attribute updated_at
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ To handle print()
        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ Returns a dictionary containing all K/V
        """

        "varible use in update to the dictionary"
        dict_C = self.__dict__.copy()
        K = ["created_at", "updated_at"]
        for KEY, V in self.__dict__.items():
            if KEY in K:
                dict_C[KEY] = V.isoformat()
        dict_C['__class__'] = self.__class__.__name__
        return dict_C
