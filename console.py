#!/usr/bin/python3
"""This is a command interpreter for the AirBnB_clone project"""


import cmd
import os
import sys
#from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    A command interpreter that prints a prompt to the console
    for the AirBnB Project
    """
    
    # custom prompt to print if in interactive mode
    prompt = "(hbnb) " if sys.stdin.isatty() else ''

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Handles the command of "End Of File" to 
        exit the program"""
        exit (0)

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        Create Command
        
        Creates a new instance of a Class.
        """
        try:
            cls = globals()[BaseModel]
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class name missing **")
        except NameError:
            print("class doesn't exist")

    def do_show(self, args):
        """
        Show Command.

        prints the string representation of an instance based on the class name and id
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
