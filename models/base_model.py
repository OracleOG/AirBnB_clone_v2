#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class that defines attributes/methods for other classes"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True, unique=True)
        created_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)
        updated_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new base model based on arguments passed

           Args:
                args: unused
                kwargs: arguments for the constructor of BaseModel

           Attributes:
                id - A unique identifier
                created_at - creation date
                update_at - update date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

        """ Previous code. For reference and study purpose
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        """

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes the current instance from the storage (models.storage)"""
        models.storage.delete(self)
