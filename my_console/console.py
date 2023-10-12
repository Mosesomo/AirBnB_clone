#!/usr/bin/python3
"""Defining a module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class definition of command"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""

        return True

    def do_EOF(self, line):
        """Handle end of file character"""

        print()
        return True

    def emptyline(self):
        """shouldn’t execute anything"""

        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """

        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            classes = storage.classes()
            new_instance = classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
            based on the class name and id
        """

        args = line.split(" ")
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
                instance = "{}.{}".format(class_name, inst_id)
                if instance not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[instance])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
            id (save the change into the JSON file)
        """

        args = line.split(" ")
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
                instance = "{}.{}".format(class_name, inst_id)
                if instance not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[instance]
                    storage.save()

    def do_all(self, line):
        """: Prints all string representation of all instances
            based or not on the class name.
        """

        if line != "":
            args = line.split(" ")
            if args[0] not in storage.classes():
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



if __name__ == "__main__":
    HBNBCommand().cmdloop()
