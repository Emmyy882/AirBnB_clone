#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
        p = Place()

    def test_default_values(self):
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)

def test_user_inheritance(self):
"""test Place to know if it is a subclass of BaseModel"""
        p = Place()
        self.assertIsInstance(p, BaseModel)

def test_has_attributes(self):
        name = "Lagos"
        user_id = "4423"
        city_id = "4411"
        description = "estate"
        number_rooms = "50"
        number_bathrooms = "50"
        max_guest = "6"
        price_by_night = "5000"
        latitude = "5.9"
        longitude = "4.4"
        amenity_ids = [444, 666, 888]
        p = Place(name=name, user_id=user_id, city_id=city_id,
                      description=description, number_rooms=number_rooms,
                      number_bathrooms=number_bathrooms, max_guest=max_guest,
                      price_by_night=price_by_night, latitude=latitude,
                      longitude=longitude, amenity_ids=amenity_ids)
        self.assertEqual(p.name, name)
        self.assertEqual(p.city_id, city_id)
        self.assertEqual(p.user_id, user_id)
        self.assertEqual(p.description, description)
        self.assertEqual(p.number_rooms, number_rooms)
        self.assertEqual(p.number_bathrooms, number_bathrooms)
        self.assertEqual(p.max_guest, max_guest)
        self.assertEqual(p.price_by_night, price_by_night)
        self.assertEqual(p.latitude, latitude)
        self.assertEqual(p.longitude, longitude)
        self.assertEqual(p.amenity_ids, amenity_ids)

def test_long_name(self):
        """verify if the class handles long names correctly"""
        name = "A" * 200
        p = Place(name=name)
        self.assertEqual(place.name, name[:355])


if __name__ == '__main__':
    unittest.main()
