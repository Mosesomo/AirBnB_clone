#!/usr/bin/python3

"""Defines the HBnB console."""

import cmd
import re
from shlex import split
from models.base_model import BaseModel
"""
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
"""


def parse(string):
    """Parse the user input."""
    return re.findall(r'[^"\']+|"[^"]+"|\'[^\']+', string)


class HBNBCommand(cmd.Cmd):
    """Command-line interface for HBnB."""

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def do_create(self, arg):
        """Create a new object."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show the details of an object."""
        args = parse(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in BaseModel.__objects:
                print(BaseModel.__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an object."""
        args = parse(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in BaseModel.__objects:
                del BaseModel.__objects[key]
                BaseModel.save_to_file()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all objects or objects of a specific class."""
        if not arg:
            objs = []
            for obj in BaseModel.__objects.values():
                objs.append(str(obj))
            print(objs)
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in BaseModel.__objects.values():
                if type(obj).__name__ == arg:
                    objs.append(str(obj))
            print(objs)

    def do_count(self, arg):
        """Count the number of objects or objects of a specific class."""
        count = 0
        if not arg:
            count = len(BaseModel.__objects)
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            for obj in BaseModel.__objects.values():
                if type(obj).__name__ == arg:
                    count += 1
        print(count)

    def do_update(self, arg):
        """Update an object with new attributes."""
        args = parse(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in BaseModel.__objects:
                obj = BaseModel.__objects[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
