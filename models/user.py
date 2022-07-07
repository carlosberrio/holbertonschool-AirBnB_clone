#!/usr/bin/python3
"""module for user class AirBnb project"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """defines all instance attributes for a User instance
        Public class attributes:
        email <string>: User's e-mailbox
        password <string>: User _Password
        fisrt_name <string>: User's firs name
        last_name <string>: User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
