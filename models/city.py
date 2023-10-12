#!/usr/bin/python3
"""Defining a module"""

from models.base_model import BaseModel


class City(BaseModel):
    """Representing class city that inherits properties
        from parent class
    """

    state_id = ""
    name = ""
