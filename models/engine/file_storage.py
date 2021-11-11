#!/usr/bin/python3
"""
create a new file storage
"""


import json
from models.base_model import BaseModel


class FileStorage():
    """ represeantation file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the Objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ storage the objects """
        rand = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(rand, obj.id)] = obj

    def save(self):
        """ serialize the objects to json file """
        dict = {i: FileStorage.__objects[i].to_dict()
                for i in FileStorage.__objects}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                reloadstor = json.load(f)
                for k, v in reloadstor.items():
                    self.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            return
