#!/usr/bin/python3
""" A script that serializes instances to a JSON file and...
    ...deserializes JSON format.
"""
import json
import os


class FileStorage():
    """serializes and deserializes instances to a JSON file.

        Private class attributes:
            __file_path: string path to the JSON file.
            __objects: dictionary to store all objects by <class name>.id
    """

    __file_path = file.json
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file(__file_path)"""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, value in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Deserializes the JSON file to __objects...
            (only if the __file_path exists; otherwise do nothing.
            if the file doesn't exist, no exception should be raised.
        """
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    obj_class = val['__class__']
                    if obj_class in classes:
                        self.__objects[key] = classes[obj_class](**val)


