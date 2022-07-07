#!/usr/bin/python3
"""Module for storage all classes,
data and storage management for the console AirBnB clone project"""

import json
from os import path
from models import review
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines the File Storage and class atributes for the new classes
    __file_path <string>: path to the JSON file
    __objects <dictionary>: stores all objects by '<class name>.id'
    __classes <dictionary>: stores all available classes for AirBnB project"""

    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        """Returns the class atribute '__objects <dictionary>'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the <obj> with key '<obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file '__file_path"""
        dict_to_json = FileStorage.__objects
        dict_to_json = {k: v.to_dict() for k, v in dict_to_json.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as jfile:
            json.dump(dict_to_json, jfile)

    def reload(self):
        """Desearlizes the JSON file to '__objects':
        checks existence of the JSON file, reads data and instantiates every
        dictionary representation according the ['__class__'] name"""
        file = FileStorage.__file_path
        if path.exists(file):
            with open(file, 'r', encoding='utf-8') as jfile:
                FileStorage.__objects = json.load(jfile)
                for key, val in FileStorage.__objects.items():
                    c = FileStorage.__objects[key]['__class__']
                    try:
                        FileStorage.__objects[key] = self.__classes[c](**val)
                    except Exception:
                        pass

    def class_dict(self):
        """Returns the class attribute '_-classes <dictionary>'
        wich strores the available Classes for all modules"""
        return FileStorage.__classes
