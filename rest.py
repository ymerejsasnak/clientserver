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

# crud operations from previous assignment
from crud import mongoCRUD


class stocksRestAPI(Bottle):
    def __init__(self):
        super(stocksRestAPI, self).__init__()

        self.route("/stocks/api/v1.0/createStock/<ticker_symbol>", method="POST", callback=self.create)
        self.route("/stocks/api/v1.0/getStock/<ticker_symbol>", method="GET", callback=self.read)
        self.route("/stocks/api/v1.0/updateStock/<ticker_symbol>", method="PUT", callback=self.update)
        self.route("/stocks/api/v1.0/deleteStock/<ticker_symbol>", method="DELETE", callback=self.delete)



    ### BASIC CRUD OPERATIONS ###


    def create(self, ticker_symbol):
      '''
      Create new document with given ticker symbol and json request
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
      Read existing document from given ticker
      '''
      try:
        result = crud.read({"Ticker" : ticker_symbol})
      except Exception as e:
        result = e
      return str(result) + "\n"


    def update(self, ticker_symbol):
      '''
      Update existing document with given ticker with new key value pairs in json request
      '''
      try:
        document = request.json
        result = crud.update({"Ticker": ticker_symbol}, document)
      except Exception as e:
        result = e
      return str(result) + "\n"


    def delete(self, ticker_symbol):
      '''
      Delete document that matches ticker_symbol
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
    rest.run(host='localhost', port=8080, reloader=True)
