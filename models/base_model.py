#!/usr/bin/python3
"""Defines a BaseModel for all common classes"""

import os
import uuid
from datetime import datetime


class BaseModel:
    """A BaseModel that defines all common attributes/methods for other classes

        Attributes:
            id (str): stores a unique id for each BaseModel
            created_at: assign with the current datatime when an instance is...
                ...created
            updated_at: assign with the current datetime when an instance is...
                ...created and will be updated every time the object is changed
    """

    id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()
    updated_at = datetime.now().isoformat()

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance for the Basemodel

        Args:
            *args: argument list with variable length.
            **kwargs: variable length of dictionary argument.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', datetime.now())
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())
        # storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def delete(self):
        """
        Deletes the BaseModel instance from the storage.

        This method removes the current instance from the storage system.
        """
        storage.delete(self)

    def save(self):
        """updates the public instance attribute updated_at with the current..
        ...datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        # call the save() method of storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of..
        ...the instance"""
        res = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value
        res['__class__'] = self.__class__.__name__
        return res


if __name__ == '__main__':
    import unittest

    class TestBaseModel(unittest.TestCase):
        """
        Test cases for the BaseModel class.
        """

        def test_init(self):
            """Tests the initialization of the BaseModel class."""
            i = BaseModel()
            self.assertIsInstance(i, BaseModel)

        def test_id(self):
            """Tests the type of id."""
            new = BaseModel()
            self.assertEqual(type(new.id), str)

        def test_created_at(self):
            """Tests the type of created_at."""
            new = BaseModel()
            self.assertEqual(type(new.created_at), datetime)

        def test_updated_at(self):
            """Tests the type of updated_at."""
            new = BaseModel()
            self.assertEqual(type(new.updated_at), datetime)

        def test_str(self):
            """
            Tests the __str__ function of the BaseModel class.
            """
            i = BaseModel()
            self.assertEqual(str(i),
                             '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

        def test_save(self):
            """Tests the save function of the BaseModel class."""
            i = BaseModel()
            i.save()
            self.assertIsNotNone(i.updated_at)

        def test_to_dict(self):
            """Tests the to_dict function of the BaseModel class."""
            i = BaseModel()
            d = i.to_dict()
            self.assertEqual(type(d), dict)
            self.assertIn('__class__', d)
            self.assertIn('id', d)
            self.assertIn('created_at', d)
            self.assertIn('updated_at', d)

    unittest.main()
