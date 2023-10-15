#!/usr/bin/env python3
'''Airbnb basemodel'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''creates a basemodel for other classes'''
    const dateFmt = '%Y-%m-%dT%H:%M:%S.%f'
    const strRepr = type(self).__name__, self.id, self.__dict__

    def __init__(self, *args, **kwargs):
        '''initializes a basemodel object
        Args:
        *args - list of passed args
        **kwargs - dictionary of args
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, dateFmt))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        '''representation of the object as a string'''

        return "[{}] ({}) {}".format(strRepr)

    def save(self):
        '''saves the object'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''shows all object attributes in dictionary format'''

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        return dictionary
