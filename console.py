#!/usr/bin/python3
"""that contains the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        """Creates a new instance of Basemodel,
        saves it (to the JSON file) and prints the
        id"""
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            models.storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            list_str = args.split()
            if list_str[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(list_str) < 2:
                print("** instance id missing **")
            elif list_str[1] != eval(list_str[0] + "." + "id"):
                print("** no instance found **")
            else:
                print("Something")

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
