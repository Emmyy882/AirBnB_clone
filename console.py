#!/usr/bin/python3
"""This is a command interpreter"""


import cmd
import os
import sys

class Interpreter(cmd.Cmd):
    """
        A command interpreter that prints a prompt to the console
        for the AirBnB Project
    """
    
    # prompt to print if in interactive mode
    prompt = "(hbnb) " if sys.stdin.isatty() else ''

    # A Dictionary that maps class names to their corresponding classes
    classes = {
            'User': User,
            'State': State,
            'City': City,
            'Place': Place
            }

