#!/usr/bin/python3
"""
Module for place class for airBnB CLone project - the console
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Defines all instance attributes for a place instance
    public class attribute:
    city_id, <string>: City.id = <Class City> + instances's id
    user_id, <string>: User.id = <Class User> + instances's id
    name <string>: Name of the place
    description <string>: description about the place
    number_rooms <int>: Number of rooms in the place
    number_bathrooms <int>: Number of bathrooms in the place
    max_guest <int> max number of guest for the place
    price_by_night <int>: price per night for the place
    latitude <float>: latitude coordinate
    longitude <float>: longitude coordinate
    amenity_ids <list of string>: List of amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
