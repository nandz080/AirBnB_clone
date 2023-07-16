#!/usr/bin/python3
"""
   Module defining reiviews class
"""
from models.base_model import BaseModel

class Review(BaseModel):
"""Class representing review that inherits from BaseModel"""

	place_id = ""
	user_id = ""
	text = ""
