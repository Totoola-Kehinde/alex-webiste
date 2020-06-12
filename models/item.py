import datetime
from schematics.models import Model
from bson.objectid import ObjectId
from flask import json, jsonify


class item(Model):
    """A class for storing Project related information"""

    def __init__(self, item_id, hyip, status, description):        
        if item_id is None:
            self._id = ObjectId()
        else:
            self._id = item_id
        self.hyip = hyip
        self.status = status
        self.description = description
        self.date = datetime.datetime.utcnow()

    def __repr__(self):
        message = {'_id':self._id,
                    'hyip':self.hyip,
                    'status':self.status,
                    'description':self.description,
                    'date':self.date
        }
        return f"{message}"

    def get_as_json(self):
        """ Method returns the JSON representation of the Item object, which can be saved to MongoDB """
        return self.__dict__
    

    @staticmethod    
    def build_from_json(json_data):
        """ Method used to build Item objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:                            
                return item(json_data['_id', None],
                    json_data['hyip'],
                    json_data['status'],
                    json_data['description'],
                    json_data['date'])
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e))
        else:
            raise Exception("No data to create Item from!")

