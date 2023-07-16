#!/usr/bin/python3

"""
Module defining city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a state that inherits from BaseModel"""

    state_id = ""
    name = ""
