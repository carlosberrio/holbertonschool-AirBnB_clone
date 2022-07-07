#!/usr/bin/python3
"""
Module for city for airBnB clone project - the console
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines all instance attributes for a city instance"""

    state_id = ""
    name = ""
