#!/usr/bin/python3
"""
Testing User
"""

from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):
    """Class test city"""

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
        new_object = City()
        self.assertEqual(str(type(new_object)), "<class 'models.city.City'>")
        self.assertIsInstance(new_object, City)
        self.assertTrue(issubclass(type(new_object), BaseModel))

    def test_attr(self):
        """test attributes"""
        attributes = {'state_id': str, 'name': str}
        new_obj = City()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_obj, k))
            self.assertEqual(type(getattr(new_obj, k, None)), value)


if __name__ == "__main__":
    unittest.main()
