#!/usr/bin/python3
'''Airbnb basemodel'''

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    '''creates a basemodel for other classes'''

    def __init__(self, *args, **kwargs):
        '''initializes a basemodel object

        Args:
            *args - list of passed args
            **kwargs - dictionary of args
        '''

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, val in kwargs.items():
                if k != '__class__':
                    if k == 'updated_at':
                        self.__dict__["updated_at"] = datetime.strptime(
                                val, '%Y-%m-%dT%H:%M:%S.%f')
                    elif k == 'created_at':
                        self.__dict__["created_at"] = datetime.strptime(
                                val, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.__dict__[k] = val

    def __str__(self):
        '''representation of the object as a string'''
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''saves the object'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''shows all object attributes in dictionary format'''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        return dictionary
