#!/usr/bin/python3
"""This module defines a class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a class user that inherits from
        parent class basemodel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
