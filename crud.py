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
from pymongo.errors import ConnectionFailure


class mongoCRUD:
    '''
    Class that wraps all functionality for interfacing with MongoDB
    '''

    def connect(self, hostname, port):
        '''
        Attempts to connect to MongoDB and
        stores the connection in self.client.

        Args:
            host_name: hostname or mongo uri (ie 'localhost')
            port: port number used
        '''
        # attempt connection
        self.client = MongoClient(hostname, port)

        # check for success using dummy command
        try:
            # The ismaster command is cheap and does not require auth.
            self.client.admin.command('ismaster')
        # exit with message on failure
        except ConnectionFailure:
            print("MongoDB connection Failure.")
            exit()


    def set_collection(self, db_name, collection_name):
        '''
        Sets the active database and collection used by
        subsequently called methods

        Args:
            db_name: database name to use
            collection_name: collection name to use
        '''
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]


    def create(self, document):
        '''
        Creates new document in current collection.

        Args:
            document: dictionary of key/value pairs to insert as document

        Returns:
            True on success
            False on failure
        '''
        try:
            self.collection.insert_one(document)
            result = True
        except Exception:
            result = False
        return result


    def read(self, query):
        '''
        Reads single document matching passed query document

        Args:
            query: dict key/value pair to use as query

        Returns:
            String dump of JSON document on success
            Exception on failure
        '''
        try:
            result = self.collection.find_one(query)
            result = json_util.dumps(result)
        except Exception as e:
            result = e
        return result


    def update(self, old, new):
        '''
        Updates document matching query "old" with key/value "new"

        Args:
            old: dictionary key/value as query to find in collection
            new: new key/value to add to item

        Returns:
            String dump of JSON document on success
            Exception on failure
        '''
        try:
            result = self.collection.update(old, {"$set" : new})
            result = json_util.dumps(result)
        except Exception as e:
            result = e
        return result


    def delete(self, query):
        '''
        Deletes document matching given query

        Args:
            query: dictionary key/value as query to search for

        Returns:
            DeleteResult on success
            Exception on fail
        '''
        try:
            doc = self.collection.find_one(query)
            result = self.collection.delete_one(doc)
        except Exception as e:
            result = e
        return result


if __name__ == '__main__':
    crud = mongoCRUD()
    crud.connect('localhost', 27017)
    crud.set_collection('market', 'stocks')
