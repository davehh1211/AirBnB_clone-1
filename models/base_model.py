#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

# STORAGE = getenv("HBNB_TYPE_STORAGE")

# if STORAGE == "db":
Base = declarative_base()
# else:
#     Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    update_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    # def __init__(self, *args, **kwargs):
    #     """Instatntiates a new model"""
    #     if not kwargs:
    #         from models import storage
    #         self.id = str(uuid.uuid4())
    #         self.created_at = datetime.now()
    #         self.updated_at = datetime.now()

    #     else:
    #         kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
    #                                                  '%Y-%m-%dT%H:%M:%S.%f')
    #         kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
    #                                                  '%Y-%m-%dT%H:%M:%S.%f')
    #         del kwargs['__class__']
    #         self.__dict__.update(kwargs)
    #         for key, value in kwargs.items():
    #             setattr(self, key, value)
    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if len(kwargs) == 0:
            # if no dictionary of attributes is passed in
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            # assign a dictionary of attributes to instance
 
            # preserve existing created_at time
            if kwargs.get('created_at'):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()  # assign current time
            if kwargs.get('updated_at'):
                # preserve existing updated_at time
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.utcnow()
 
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())
 
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    # def to_dict(self):
    #     """Convert instance into dict format"""
    #     dictionary = {}
    #     dictionary.update(self.__dict__)
    #     dictionary.update({'__class__':
    #                        (str(type(self)).split('.')[-1]).split('\'')[0]})
    #     dictionary['created_at'] = self.created_at.isoformat()
    #     dictionary['updated_at'] = self.updated_at.isoformat()
    #     for key, value in dictionary.items():
    #         if key == '_sa_instance_state':
    #             del dictionary[key]
    #     return dictionary
    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        if 'updated_at' in cp_dct:
            cp_dct['updated_at'] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        if 'created_at' in cp_dct:
            cp_dct['created_at'] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        if '_sa_instance_state' in cp_dct:
            cp_dct.pop('_sa_instance_state', None)
        return (cp_dct)

    def delete(self):
        """[summary]
        """
        from models import storage
        storage.delete(self)
