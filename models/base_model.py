#!/usr/bin/python3
'''Airbnb basemodel'''

import uuid
from datetime import datetime


class BaseModel:
    '''creates a basemodel for other classes'''

    def __init__(self, *args, **kwargs):
        '''initializes a basemodel object

        Args:
            *args - list of passed args
            **kwargs - dictionary of args
        '''

        if kwargs is not None and kwargs != {}:
            for k, val in kwargs.items():
                if k == 'updated_at':
                    self.__dict__["updated_at"] = datetime.strptime(
                            val, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'created_at':
                    self.__dict__["created_at"] = datetime.strptime(
                            val, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''representation of the object as a string'''

        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''saves the object'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''shows all object attributes in dictionary format'''

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        return dictionary
