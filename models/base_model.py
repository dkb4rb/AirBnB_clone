#!/usr/bin/python3
"""
Import Libraries and moduls
"""
import models
from time import time
from uuid import uuid4
from datetime import datetime
from time import sleep


class BaseModel:
    """ Represent new class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """ Instantiation BaseModel
        """

        date = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for v, f in kwargs.items():
                if v == "created_at" or v == "update_at":
                    self.__dict__[v] = datetime.strptime(f, date)
                else:
                    self.__dict__[v] = f
        else:
            models.storage.new(self)

    def save(self):
        """ Update the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Return the dictionary of the BaseModel"""
        dictionary = self.__dict__
        dictionary["__class__"] = BaseModel.__name__
        if type(dictionary["created_at"]) is not str:
            dictionary["created_at"] = self.created_at.isoformat()
        if type(dictionary["updated_at"]) is not str:
            dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return The print in str the representation
        of the Instance BaseModel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
