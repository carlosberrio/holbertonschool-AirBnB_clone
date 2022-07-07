#!/usr/bin/python3
"""
Module for basemodel class
defines all common attributes/methods for other classes
for airbnb clone project - the console
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Class that define all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialities base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a good print of the base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the date of update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a new dict"""
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = type(self).__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
