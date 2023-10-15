#!/usr/bin/python3
"""A script of a class that inherits from another class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This Class inherits from BaseModel class

    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
