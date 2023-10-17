#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes(self):
        name = "Imo"
        state = State(name=name)
        self.assertEqual(state.name, name)

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_long_name(self):
        """Verify if the class handles long names correctly"""
        name = "A" * 200
        state = State(name=name)
        self.assertEqual(state.name, name[:355])


if __name__ == '__main__':
    unittest.main()
