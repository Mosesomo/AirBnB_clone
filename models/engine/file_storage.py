#!/usr/bin/python3
"""
Defining a file storage class
"""
import json
import os
from models.base_model import BaseModel
"""
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
"""


class FileStorage:
    """Represents an abstracted storage engine.
    Attributes:
        __file_path (str): filename to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __filepath = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__filepath, 'w', encoding="utf-8") as file:
            serialized_objects = {}
            for key, obj in FileStorage.__objects.items():
                serialized_objects[key] = obj.to_dict()
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__filepath):
            with open(FileStorage.__filepath, 'r') as file:
                serialized_objects = json.load(file)
                for key, serialized_obj in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)()
                    obj.__dict__ = serialized_obj
                FileStorage.__objects[key] = obj
