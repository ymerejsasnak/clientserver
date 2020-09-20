'''
Jeremy Kansas
CS 499
Artifact 1 part 1 of 2
Python to MongoDB interface
Used as part of Category 1 and 3
'''


import json
from bson import json_util
from pymongo import MongoClient




class mongoCRUD:
    '''
    Class that wraps all functionality for interfacing with MongoDB
    '''

    def __init__(self):
        # connect to mongodb and store the connection
        self.connection = MongoClient('localhost', 27017)

        # specifcy db and collection to use
        self.db_name = 'market'
        self.collection_name = 'stocks'
        self.db = self.connection[self.db_name]
        self.collection = self.db[self.collection_name]


    ## BASIC CRUD OPERATIONS ##

    def create(self, document):
        '''
        <FINAL 2 A> Insert new document into 'collection'
        Returns True on success, False on fail
        '''
        try:
            self.collection.insert_one(document)
            result = True
        except Exception:
            result = False
        return result


    def read(self, query):
        '''
        Read single document matching passed query document
        Return JSON document, or given exception on failure
        '''
        try:
            result = self.collection.find_one(query)
            result = json_util.dumps(result)
        except Exception as e:
            result = e
        return result


    def update(self, old, new):
        '''
        Update document matching 'old' query with 'new' key/value
        Return JSON doc on success, exception on failure
        '''
        try:
            result = self.collection.update(old, {"$set" : new})
            result = json_util.dumps(result)
        except Exception as e:
            result = e
        return result


    def delete(self, query):
        '''
        Delete document matching given query
        Return JSON result on success, exception on fail
        '''
        try:
            doc = self.collection.find_one(query)
            result = self.collection.delete_one(doc)
        except Exception as e:
            result = e
        return result
