#!/usr/bin/python3
"""Defines a BaseModel for all common classes"""
import uuid


class BaseModel:
    """A BaseModel that defines all common attributes/methods for other classes"""
    id = f'{uuid.uuid4()}'
