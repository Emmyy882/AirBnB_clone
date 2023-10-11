#!/usr/bin/python3
"""This is a command interpreter"""


import cmd
import os

class Interpreter(cmd.Cmd):
    """A command interpreter that prints a prompt to the console"""
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''
