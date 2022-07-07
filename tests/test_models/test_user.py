#!/usr/bin/python3
"""
Testing User
"""

from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """Class test user"""

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
        new_object = User()
        self.assertEqual(str(type(new_object)), "<class 'models.user.User'>")
        self.assertIsInstance(new_object, User)
        self.assertTrue(issubclass(type(new_object), BaseModel))

    def test_attr(self):
        """test attributes"""
        attributes = {'email': str, 'password': str,
                      'first_name': str, 'last_name': str}
        new_obj = User()
        for k, value in attributes.items():
            self.assertTrue(hasattr(new_obj, k))
            self.assertEqual(type(getattr(new_obj, k, None)), value)


if __name__ == "__main__":
    unittest.main()
