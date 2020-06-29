#!/usr/bin/python3
"""Our BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel():
    """The main class"""

    def __init__(self, *args, **kwargs):
        """Constructor of the instance"""
        if kwargs is True:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at" or key == "updated_at":
                        datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return an user friendly representation
           of the isinstance
        """
        return ("[{}] ({}) {}]".format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute
        updated_at with the current date and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing
        all the __dict__ keys / values of the instance"""
        my_dict = self.__dict__
        my_dict.update({"__class__": self.__class__.__name__})
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        return (my_dict)
