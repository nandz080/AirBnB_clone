#!/usr/bin/python3
"""Module defining reiviews class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Class representing review that inherits from BaseModel
     Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

