#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        Attributes:
            id (str): The BaseModel id.
            created_at (datetime): The datetime at which the BaseModel was
            created. 
            updated_at (datetime): The datetime at which the BaseModel was
            last updated.   
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for attribute, value in kwargs.items():
                if attribute == "created_at" or attribute == "updated_at":
                    self.__dict__[attribute] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[attribute] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime.
        Calls the storage save method to save the BaseModel instance to the
        JSON file.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance.
        Includes the key/value pair '__class__' representing the class name.
        Converts 'created_at' and 'updated_at' to strings in ISO format.
        Returns:
            dict: Dictionary of the BaseModel instance attributes.
        """
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj

    def __str__(self):
        """Return the string representation of the BaseModel instance.
        Returns:
            str: The string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

