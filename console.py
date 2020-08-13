#!/usr/bin/python3
"""The command interpreter for the Back-End"""

import cmd
import models
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "
    allowed_obj = ["BaseModel",
                   "User",
                   "Amenity",
                   "City",
                   "Place",
                   "Review",
                   "State"]

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file"""
        return True

    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id."""
        my_list = args.split()
        if not my_list:
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        else:
            my_object = eval(my_list[0] + '()')

            for i in range(1, len(my_list)):
                res = my_list[i].split('=')
                res[1] = res[1].replace('_', ' ')
                setattr(my_object, res[0], res[1])

            my_object.save()
            print(my_object.id)


    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            instance = list_str[0] + '.' + list_str[1]
            if instance in objects.keys():
                print(objects[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            instance = list_str[0] + '.' + list_str[1]
            if instance in objects.keys():
                del(objects[instance])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        list_str = args.split()
        if not args or list_str[0] in HBNBCommand.allowed_obj:
            str_list = []
            objects = models.storage.all()
            for instance in objects.values():
                str_list.append(instance.__str__())
            print(str_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        elif len(list_str) == 2:
            print("** attribute name missing **")
        elif len(list_str) == 3:
            print("** value missing **")
        else:
            objects = models.storage.all()
            instance = "{}.{}".format(list_str[0], list_str[1])
            if instance in objects.keys():
                for value in objects.values():
                    try:
                        attr_type = type(getattr(value, list_str[2]))
                        list_str[3] = attr_type(list_str[3])
                    except AttributeError:
                        pass
                setattr(value, list_str[2], list_str[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        '''empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
