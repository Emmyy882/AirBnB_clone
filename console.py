#!/usr/bin/python3
"""This is a command interpreter for the AirBnB_clone project"""


import cmd
import os
import sys

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
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
