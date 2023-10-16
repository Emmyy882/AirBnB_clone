#!/usr/bin/python3
"""Defines the city class"""
from .base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from BaseModel

    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
