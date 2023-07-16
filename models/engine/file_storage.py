#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                dict_obj = json.load(f)
                for o in dict_obj.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return

        with open(FileStorage.__file_path, "r") as file:
            content = file.read()
            if content is None:
                return
            objects_dict = json.loads(content)
            FileStorage.__objects = {}
            for key, value in objects_dict.items():
                if "User" in key:
                    FileStorage.__objects[key] = User(**objects_dict[key])
                    continue
                elif "State" in key:
                    FileStorage.__objects[key] = State(**objects_dict[key])
                    continue
                elif "City" in key:
                    FileStorage.__objects[key] = City(**objects_dict[key])
                    continue
                elif "Place" in key:
                    FileStorage.__objects[key] = Place(**objects_dict[key])
                    continue
                elif "Amenity" in key:
                    FileStorage.__objects[key] = Amenity(**objects_dict[key])
                    continue
                elif "Review" in key:
                    FileStorage.__objects[key] = Review(**objects_dict[key])
                    continue
                FileStorage.__objects[key] = BaseModel(**objects_dict[key])
