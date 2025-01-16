#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import models
from os import getenv


class State(BaseModel, Base):
    """ State for MySQL DB

        Inherits from MySQLQlchemy Base to MySQL tables

        Attribute:
        __tablename__(str): Name of MySQL table storing states
        name (str): Name of state
        city (sqlalchemy relationship): State-City order.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Gets list of city instances with the current state_id
        Getter attribute for Filestorage
        relationship btw states and cities
        """
        cities_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
