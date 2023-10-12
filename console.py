#!/usr/bin/python3
"""Defining a module"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new object."""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            classes = storage.classes()
            obj = classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show the details of an object."""
        args = arg.split(" ")
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                inst_id = args[1]
                key = "{}.{}".format(class_name, inst_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an object."""

        args = arg.split(" ")
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                inst_id = args[1]
                key = "{}.{}".format(class_name, inst_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


    def do_all(self, arg):
        """Show all objects or objects of a specific class."""
        
        if arg != "":
            args = arg.split(" ")
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                inst_list = []
                for k, v in storage.all().items():
                    v = str(v)
                    inst_list.append(v)
                print(inst_list)
        else:
            inst_list = []
            for k, v in storage.all().items():
                 v = str(v)
                 inst_list.append(v)
            print(inst_list)

    def do_update(self, arg):
        """Update an object with new attributes."""
        args = arg.split(" ")
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                obj = storage.all()[key]
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
