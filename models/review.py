#!/usr/bin/python3
"""Defining a module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a class Review"""

    place_id = ""
    user_id = ""
    text = ""
