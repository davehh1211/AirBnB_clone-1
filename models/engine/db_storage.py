#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
import sqlalchemy
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {'State': State, 'City': City}


class DBStorage:
    """return a dictionary

    Returns:
    [type]: [description]
    """
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PASSWORD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER,
            PASSWORD,
            HOST,
            DB), pool_pre_ping=True)
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict_new = {}
        if cls is None:
            for cla in classes:
                obj = self.__session.query(classes[cla])
                for itm in obj:
                    delattr(itm, '_sa_instance_state')
                    key = itm.__class__.__name__ + '.' + itm.id
                    dict_new[key] = itm
        else:
            for cla in classes:
                if cla == cls:
                    obj = self.__session.query(classes[cla])
                    for itm in obj:
                        delattr(itm, '_sa_instance_state')
                        key = itm.__class__.__name__ + '.' + itm.id
                        dict_new[key] = itm
        return dict_new

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is None:
            self.__session.detele(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_weak = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_weak)
