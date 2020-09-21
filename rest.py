#!/usr/bin/python

'''
Jeremy Kansas
CS 499
Artifact 1 part 2 of 2
Microserver with RESTful API
Used as part of Category 1 and 3
'''


import json
from bson import json_util
import datetime
import bottle
from bottle import route, run, request, abort, put, Bottle

# mongo interface class from crud.py
from crud import mongoCRUD


class stocksRestAPI(Bottle):
    '''
    Class that inherits from Bottle to implement simple server
    with RESTful API for each CRUD operation in crud.py/mongoCRUD
    '''

    def __init__(self):
        super(stocksRestAPI, self).__init__()


    def route(self):
        '''
        Sets up routing url and callback method for each HTTP request
        '''
        self.route("/stocks/api/v1.0/createStock/<ticker_symbol>", method="POST", callback=self.create)
        self.route("/stocks/api/v1.0/getStock/<ticker_symbol>", method="GET", callback=self.read)
        self.route("/stocks/api/v1.0/updateStock/<ticker_symbol>", method="PUT", callback=self.update)
        self.route("/stocks/api/v1.0/deleteStock/<ticker_symbol>", method="DELETE", callback=self.delete)


    def create(self, ticker_symbol):
        '''
        Creates new document with given json request and ticker ticker_symbol

        Header:  "Content-Type: application/json"
        Method:  POST
        Body Data:  Key/value JSON document
        URL:  http://<host>:<port>/stocks/api/v1.0/createStock/<ticker_symbol>

        Example curl command (line breaks for readability):
        curl -H "Content-Type: application/json" -X POST -d
        '{"Sector" : "CREATE TEST","Industry" : "CREATE TEST"}'
        http://localhost:8080/stocks/api/v1.0/createStock/ZZZZZ

        Returns:
            result as string
        '''
        try:
            document = request.json
            document["Ticker"] = ticker_symbol
            result = crud.create(document)
        except Exception as e:
            result = e
        return str(result) + "\n"


    def read(self, ticker_symbol):
        '''
        Reads existing document from given ticker

        Header: None
        Method: GET
        Body Data: None
        URL: http://<host>:<port>/stocks/api/v1.0/getStock/<ticker_symbol>

        Example curl command:
        curl http://localhost:8080/stocks/api/v1.0/getStock/ZZZZZ

        Returns:
            result as string
        '''
        try:
            result = crud.read({"Ticker" : ticker_symbol})
        except Exception as e:
            result = e
        return str(result) + "\n"


    def update(self, ticker_symbol):
        '''
        Updates existing document with given ticker with new key value pairs in json request

        Header: "Content-Type: application/json"
        Method: PUT
        Body Data: Key/value JSON document
        URL: http://<host>:<port>/stocks/api/v1.0/updateStock/<ticker_symbol>

        Example curl command (line breaks for readability):
        curl -H "Content-Type: application/json" -X PUT -d
        '{"Sector" : "UPDATE TEST", "Industry" : "UPDATE TEST"}'
        http://localhost:8080/stocks/api/v1.0/updateStock/ZZZZZ

        Returns:
            result as string
        '''
        try:
            document = request.json
            result = crud.update({"Ticker": ticker_symbol}, document)
        except Exception as e:
            result = e
        return str(result) + "\n"


    def delete(self, ticker_symbol):
        '''
        Deletes document that matches ticker_symbol

        Header: None
        Method: GET
        Body Data: None
        URL: http://<host>:<port>/stocks/api/v1.0/getStock/<ticker_symbol>

        Example curl command:
        curl -X DELETE http://localhost:8080/stocks/api/v1.0/deleteStock/ZZZZZ

        Returns:
            result as string
        '''
        try:
            result = crud.delete({"Ticker" : ticker_symbol})
        except Exception as e:
            result = e
        return str(result) + "\n"




if __name__ == '__main__':
    crud = mongoCRUD()
    crud.connect('localhost', 27017)
    crud.set_collection('market', 'stocks')

    rest = stocksRestAPI()
    rest.route()
    rest.run(host='localhost', port=8080, reloader=True)
