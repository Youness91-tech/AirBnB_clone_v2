#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Class manages storage of hbnb models in JSON format """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage """
        if not cls:
            return FileStorage.__objects
        elif isinstance(cls, str):
            return {
                key: value for key, value in self.__objects.items()
                if value.__class__.__name__ == cls
            }
        else:
            return {
                key: value for key, value in self.__objects.items()
                if value.__class__ == cls
            }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            my_dict = {}
            my_dict.update(FileStorage.__objects)
            for key, val in my_dict.items():
                my_dict[key] = val.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything
        """
        if obj is not None:
            obj_Key = obj.__class__.__name__ + "." + obj.id
            del self.__objects[obj_Key]
            self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
