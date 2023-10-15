#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage
"""
from models.engine.file_storage import FileStorage

# Create the storage instance
storage = FileStorage()

# Call the reload() method on the storage instance
storage.reload()
