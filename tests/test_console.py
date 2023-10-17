#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

import unittest
import os
import sys
import re
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_all
    TestHBNBCommand_show
    TestHBNBCommand_create
    TestHBNBCommand_exit
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

 def test_help_quit(self):
     """Tests the help command."""
     s = "Quit command to exit the program\n"
     with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_create(self):
        """Tests the help command."""
        s = ("Usage: create <class>\n        "
             "Create a new class instance")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_all(self):
    """Tests the help command."""
    s = "Display all instances based on the class name\n"
    with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_show(self):
    """Tests the help command."""
    s = "Display the string representation of objects\n"
    with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_EOF(self):
        """Tests the help command."""
        s = "EOF signal to exit the program\n"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_destroy(self):
        """Tests the help command."""
        s = "Deletes a class instance based on the class name and id\n"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_count(self):
        """Tests the help command."""
        s = "Counts the number of instances of a given class.\n"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(s, output.getvalue().strip())

def test_help_update(self):
        """Tests the help command."""
        s = "Update a class instance of a given object\n"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(s, output.getvalue().strip())

def test_help(self):
        """Tests the help command."""
        s = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(s, output.getvalue().strip())
