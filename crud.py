'''
Jeremy Kansas
CS 499
Artifact 1 of 2
Python to MongoDB interface
Used as part of Category 1 and 3
'''


import json
from bson import json_util
from pymongo import MongoClient




class mongoCRUD:
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


     ### SPECIALIZED OPERATIONS ###

    def update_volume(self, ticker, new_volume):
        '''
        <FINAL 2 B> Update function that specifically matches a Ticker and updates its Volume with a value greater than 0
        '''

        if new_volume <= 0:
            result = "Volume must be greater than zero."

        else:
            try:
                result = self.update({"Ticker": ticker}, {"Volume": new_volume})
            except Exception as e:
                result = e

        return result


    def delete_ticker(self, ticker):
        '''
        <FINAL 2 C> Delete function that deletes document with given ticker
        '''
        try:
            result = self.delete({"Ticker": ticker})
        except Exception as e:
            result = e

        return result



    def fifty_day_count(self, low, high):
        '''
        <FINAL 3 A i> find and count all documents with a 50-day simple moving average within the given range (low, high)
        '''
        try:
            docs = self.collection.find({"50-Day Simple Moving Average" : {"$gt" : low, "$lt" : high } })
            result = docs.count()
        except Exception as e:
            result = e
        return result


    def find_by_industry(self, industry):
        '''
        <FINAL 3 A ii> get list of all Ticker strings in a given industry
        '''
        try:
            docs = self.collection.find({"Industry" : industry})
            result = docs.distinct("Ticker")
        except Exception as e:
            result = e
        return result


    def outstanding_shares(self, sector):
        '''
        <FINAL 3 B> find total outstanding shares in a sector, grouped by industry
        '''
        try:
            result = self.collection.aggregate([
                {"$match": {"Sector": sector} },
                {"$group": {"_id": "$Industry", "Total Shares Outstanding": {"$sum" : "$Shares Outstanding"} } }
            ])
        except Exception as e:
            result = e
        return result # not sure what is expected output here -- currently if try succeeds, result will be a pymongo cursor
