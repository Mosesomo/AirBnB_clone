#!/usr/bin/python3
"""
Defining a file storage class
"""
import json
import os

"""
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

    def classes(self):
        """Returns a dictionary of classes"""

        from models.base_model import BaseModel
        from models.user import User

        return {
                "BaseModel": BaseModel,
                "User": User
                }

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if not os.path.isfile(FileStorage.__filepath):
            return
        with open(FileStorage.__filepath, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            classes = self.classes()
            obj_dict = {key: classes[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
