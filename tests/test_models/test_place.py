#!/usr/bin/python3
"""
Testing User
"""

from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):
    """Class test place"""

    def setUp(self):
        """Method setup"""
        pass

    def resetStorage(self):
        """method reset storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """method teardown"""
        self.resetStorage()
        pass

    def test_instance(self):
        """test instance"""
        new_object = Place()
        self.assertEqual(str(type(new_object)), "<class 'models.place.Place'>")
        self.assertIsInstance(new_object, Place)
        self.assertTrue(issubclass(type(new_object), BaseModel))

    def test_attr(self):
        """test attributes"""
        attributes = {'city_id': str, 'user_id': str, 'name': str,
                      'description': str, 'number_rooms': int,
                      'number_bathrooms': int, 'max_guest': int,
                      'price_by_night': int, 'latitude': float,
                      'longitude': float, 'amenity_ids': list}
        new_obj = Place()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_obj, k))
            self.assertEqual(type(getattr(new_obj, k, None)), value)


if __name__ == "__main__":
    unittest.main()
