#!/usr/bin/python

'''
Jeremy Kansas
CS 340
Final
'''



import json
from bson import json_util
import datetime
import bottle
from bottle import route, run, request, abort, put

# crud operations from previous assignment
import crud


def json_helper(string):
  return json.loads(json.dumps(string, indent=4, default=json_util.default)) + "\n"



### BASIC CRUD OPERATIONS ###

@route("/stocks/api/v1.0/createStock/<ticker_symbol>", method="POST")
def create(ticker_symbol):
  '''
  Create new document with given ticker symbol and json request
  '''
  try:
    document = request.json
    document["Ticker"] = ticker_symbol
    result = crud.insert(document)
  except Exception as e:
    result = e
  return str(result) + "\n"

@route("/stocks/api/v1.0/getStock/<ticker_symbol>", method="GET")
def read(ticker_symbol):
  '''
  Read existing document from given ticker
  '''
  try:
    result = crud.read({"Ticker" : ticker_symbol})
  except Exception as e:
    result = e
  return str(result) + "\n"

@route("/stocks/api/v1.0/updateStock/<ticker_symbol>", method="PUT")  
def update(ticker_symbol):
  '''
  Update existing document with given ticker with new key value pairs in json request
  '''
  try:
    document = request.json
    result = crud.update({"Ticker": ticker_symbol}, document)
  except Exception as e:
    result = e
  return str(result) + "\n"

@route("/stocks/api/v1.0/deleteStock/<ticker_symbol>", method="DELETE")
def delete(ticker_symbol):
  '''
  Delete document that matches ticker_symbol
  '''
  try:
    result = crud.delete({"Ticker" : ticker_symbol})
  except Exception as e:
    result = e
  return str(result) + "\n"


### SPECIALIZED OPERATIONS ###

@route("/stocks/api/v1.0/stockReport", method="POST")
def stock_report():
  '''
  Return a list of stock documents for each ticker in a json request list
  '''
  try:
    ticker_list = request.json
    result = []
    # get the doc for each ticker and append it to result list
    for ticker in ticker_list: 
      result.append(read(ticker))
    result = "\n".join(result) # this line is only to add spaces between documents to make screenshot more readable 
  except Exception as e:
    result = e
  return str(result) + "\n"

@route("/stocks/api/v1.0/industryReport/<industry>")
def industry_report(industry):
  '''
  Return the top five stocks in a given industry
  (many possible metrics to use, currently this is based solely on "Return on Investment" field)
  '''
  try:
    # get list of all tickers in an industry
    ticker_list = crud.find_by_industry(industry)
    result = []
  
    # iterate through the tickers and build a list of {ticker, ROI} dictionaries
    for ticker in ticker_list:
      result.append({"Ticker": ticker, "ROI": json.loads(read(ticker))["Return on Investment"]})

    # sort that list, highest to lowest, based on the ROI value
    result = sorted(result, key=lambda k: k["ROI"], reverse=True)
    
    # return only the first 5 (as a string)
    result = result[:5]
    
  except Exception as e:
    result = e
    
  return str(result) + "\n"
  
  
  
    


if __name__ == '__main__':
  run(host='localhost', port=8080, reloader=True)