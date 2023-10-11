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
            update_at: assign with the current datetime when an instance is...
                ...created and will be updated every time the object is changed
    """

    id = f'{uuid.uuid4()}'
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


    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        cls = self.__class__.__name__
        return f'[cls] (self.id) self.__dict__'

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of..
        ...the instance"""
        return {
                'id': sel
