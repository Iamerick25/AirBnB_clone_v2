#!/usr/bin/python3
""" new class for sqlAlchemy """
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
=======
        """
        create engine
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                          os.getenv('HBNB_MYSQL_USER'),
                                          os.getenv('HBNB_MYSQL_PWD'),
                                          os.getenv('HBNB_MYSQL_HOST'),
                                          os.getenv('HBNB_MYSQL_DB')),
                                          pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
>>>>>>> 9dcef72d74c0f8d6b7e183b3e98da779363bef24
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls:
            return self.__session.query(cls).all()
        else:
            return {
                f"{obj.__class__.__name__}.{obj.id}": obj
                for obj in self.__session.query(Base)
            }
    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()
    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """configuration
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.remove()
