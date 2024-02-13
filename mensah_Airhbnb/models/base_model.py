#!/usr/bin/python3
""" base model"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ class basemodel"""
    def __init__(self, *args, **kwargs) -> None:
        """ init method"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                self.__dict__[key] = value
        else:
            self.id : str = str(uuid4())
            self.created_at : datetime = datetime.today()
            self.updated_at : datetime = datetime.today()
    
    def __str__(self) -> str:
        """ string repr"""
        classname = self.__class__.__name__
        str = "[{}] ({}) {}".format(classname, self.id, self.__dict__)
        return str
    
    def save(self):
        """ update time """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """dict updaste """
        classname = self.__class__.__name__
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = classname
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        return copy_dict
        
        
        