#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        list_city = []
        all_ins = storage.__objects
        for key, value in all_ins.items():
            key_list = key.split(".")
            if key_list[0] == "City":
                if value.to_dict()["state_id"] == self.id:
                    list_city.append(value)
        return list_city
