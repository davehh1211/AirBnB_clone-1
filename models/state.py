#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if STORAGE == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='state', cascade="all, delete-orphan")

        @property
        def cities(self):
            from models import storage
            list_city = []
            all_ins = storage.all(City)
            for value in all_ins.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
    else:
        name = ""
