#!/usr/bin/python3
"""module for Review class AirBnb project"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines all attributes for a Review Instance
       Public class attributes:
       Place_id <string>: Place.id = <Class Place> + instance´s id
       user_id <string>: User.id = <Class User> + instance´s id
       text <string>: User´s Review
    """
    place_id = ""
    user_id = ""
    text = ""
