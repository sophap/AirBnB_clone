#!/usr/bin/env python3
"""FIlestorage class item"""

import datetime
import os
import json


class FileStorage:
    """class to store data"""

    __file_path: "file.json"
    __objects: {}

    def all(self):
        """get dict objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj with key <obj class name>.id in __objects"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as filed:
            dic = {ke: v.to_dict() for ke, v in FileStorage.__objects.items()}
            json.dump(dic, filed)

    def classes(self):
        """dict of classes"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as filed:
            dic = json.load(filed)
            dic = {ki: self.classes()[v["__class__"]](**v)
                    for ki, v in dic.items()}
            FileStorage.__objects = dic

    def attributes(self):
        """returns attributes and its types"""
        attributes = {
                "BaseModel": {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                    },
                "User": {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str
                    },
                "State": {"name": str},
                "City": {"state_id": str,
                    "name": str,
                    },
                "Amenity": {"name": str},
                "Place": {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "Review": {"place_id": str,
                    "user_id": str,
                    "text": str}
                return attributes
