#!/usr/bin/python3
"""
Documentation for module review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for place"""
    place_id = ""
    user_id = ""
    text = ""
