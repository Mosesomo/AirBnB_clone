#!/usr/bin/python3
# This module define a class BaseModel

import uuid
from datetime import datetime


class BaseModel:
    """Representing the base class model"""

    def __init__(self):
        """This function initializes instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the string representation"""

        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """

        self.update_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance:
        """

        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()

        return dict_obj
