#!/usr/bin/python3
"""
Unit tests for amenity.py
"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
"""Tests instances from amenity class"""

def test_user_inheritance(self):
amenity = Amenity()
"""test if Amenity is a subclass of BaseModel"""
self.assertIsInstance(amenity, BaseModel)

def test_attributes(self):
"""verify if attributes exist"""
        name = "chair"

        amenity = Amenity(name=name)
        self.assertEqual(amenity.name, name)

def test_is_subclass(self):
        self.assertTrue(issubclass(name.amenity.__class__, BaseModel), True)

def test_types(self):
        """verify if the type of attribute is correct"""
        self.assertIsInstance(amenity.name, str)
        self.assertIsInstance(name.amenity.id, str)
        self.assertIsInstance(name.amenity.created_at, datetime.datetime)
        self.assertIsInstance(name.amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
