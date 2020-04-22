#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""
        @property
        def cities(self):
            """returns a list of city"""
            all_cities = models.storage.all(City)
            list_cities = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
