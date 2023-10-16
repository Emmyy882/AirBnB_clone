#!/usr/bin/python3
"""Defines the class Review"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from BaseModel

    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
