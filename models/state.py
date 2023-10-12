#!/usr/bin/python3
"""Defining a module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representing a class state that inherits from
        parent class BaseModel
    """

    name = ""
