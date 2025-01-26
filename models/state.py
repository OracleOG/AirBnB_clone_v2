#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                            backref="state")
    else:
        @property
        def get_cities(self):
            obj = models.storage.all(City)
            ls = [v for k, v in obj.items() if v.state_id == self.id]
            sorted(ls, key=lambda city: city.name)
            return ls
