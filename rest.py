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

        self.route("/stocks/api/v1.0/stockReport", method="POST", callback=self.stock_report)
        self.route("/stocks/api/v1.0/industryReport/<industry>", callback=self.industry_report)

        self.crud = mongoCRUD()

    ### BASIC CRUD OPERATIONS ###


    def create(self, ticker_symbol):
      '''
      Create new document with given ticker symbol and json request
      '''
      try:
        document = request.json
        document["Ticker"] = ticker_symbol
        result = self.crud.create(document)
      except Exception as e:
        result = e
      return str(result) + "\n"


    def read(self, ticker_symbol):
      '''
      Read existing document from given ticker
      '''
      try:
        result = self.crud.read({"Ticker" : ticker_symbol})
      except Exception as e:
        result = e
      return str(result) + "\n"


    def update(self, ticker_symbol):
      '''
      Update existing document with given ticker with new key value pairs in json request
      '''
      try:
        document = request.json
        result = self.crud.update({"Ticker": ticker_symbol}, document)
      except Exception as e:
        result = e
      return str(result) + "\n"


    def delete(self, ticker_symbol):
      '''
      Delete document that matches ticker_symbol
      '''
      try:
        result = self.crud.delete({"Ticker" : ticker_symbol})
      except Exception as e:
        result = e
      return str(result) + "\n"


    ### SPECIALIZED OPERATIONS ###

    #!!!! THESE DON'T WORK CORRECTLY YET 


    def stock_report(self):
      '''
      Return a list of stock documents for each ticker in a json request list
      '''
      try:
        ticker_list = request.json
        result = []
        # get the doc for each ticker and append it to result list
        for ticker in ticker_list:
          result.append(self.crud.read(ticker))
        result = "\n".join(result) # this line is only to add spaces between documents to make screenshot more readable
      except Exception as e:
        result = e
      return str(result) + "\n"


    def industry_report(self, industry):
      '''
      Return the top five stocks in a given industry
      (many possible metrics to use, currently this is based solely on "Return on Investment" field)
      '''
      try:
        # get list of all tickers in an industry
        ticker_list = self.crud.find_by_industry(industry)
        result = []

        # iterate through the tickers and build a list of {ticker, ROI} dictionaries
        for ticker in ticker_list:
          result.append({"Ticker": ticker, "ROI": json.loads(self.crud.read(ticker))["Return on Investment"]})

        # sort that list, highest to lowest, based on the ROI value
        result = sorted(result, key=lambda k: k["ROI"], reverse=True)

        # return only the first 5 (as a string)
        result = result[:5]

      except Exception as e:
        result = e

      return str(result) + "\n"






if __name__ == '__main__':
    rest = stocksRestAPI()
    rest.run(host='localhost', port=8080, reloader=True)
