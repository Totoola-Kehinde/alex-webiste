from models.item import item
from pymongo import MongoClient
from bson.objectid import ObjectId
import settings


class itemRepository(item):
    """ Repository implementing CRUD operations on items collection in MongoDB """

    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI) 
        self.db = self.client[settings.MONGO_DB]

    def create(self, item):
        if item is not None:
            return self.db.items.insert(item.get_as_json())            
        else:
            raise Exception("Nothing to save, because item parameter is None")

    def read(self, id=None):
        if id is None:
            return self.db.items.find({})
        else:
            return self.db.items.find({"_id":ObjectId(id)})

    def update(self, item):
        if item is not None:
            # the save() method updates the document if this has an _id property 
            # which appears in the collection, otherwise it saves the data
            # as a new document in the collection
            return self.db.items.save(item.get_as_json())            
        else:
            raise Exception("Nothing to update, because item parameter is None")

    def delete(self, item):
        if item is not None:
            self.db.items.remove(item.get_as_json())         
        else:
            raise Exception("Nothing to delete, because item parameter is None")
