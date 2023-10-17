#!/usr/bin/python3
""" A script that serializes instances to a JSON file and...
    ...deserializes JSON format.
"""
import json
import os
from importlib import import_module


class FileStorage():
    """serializes and deserializes instances to a JSON file.

        Private class attributes:
            __file_path: string path to the JSON file.
            __objects: dictionary to store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance."""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file(__file_path)"""
        temp = {}
        with open(self.__file_path, 'w') as file:
            for key, value in self.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, file)

    def delete(self, obj=None):
        """
        Removes an object from the storage dictionary.

        Args:
            obj (BaseModel, optional): The object to delete. Defaults to None.
        """
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def reload(self):
        """Deserializes the JSON file to __objects...
            (only if the __file_path exists; otherwise do nothing.
            if the file doesn't exist, no exception should be raised.
        """
        classes = self.model_classes
        if os.path.isfile(FileStorage.__file_path):
            temp = {}
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    obj_class = value['__class__']
                    if obj_class in classes:
                        self.__objects[key] = classes[obj_class](**value)
        else:
            return

    def close(self):
        """Closes the storage engine"""
        self.reload()
