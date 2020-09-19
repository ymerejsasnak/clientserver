'''
Jeremy Kansas
CS 340
Final
'''


import json
from bson import json_util
from pymongo import MongoClient

# connect to mongodb and store the connection
connection = MongoClient('localhost', 27017)

# specifcy db and collection to use
db_name = 'market'
collection_name = 'stocks'
db = connection[db_name]
collection = db[collection_name]


# basic crud operations

def insert(document):
  '''
  <FINAL 2 A> Insert new document into 'collection'
  Returns True on success, False on fail
  '''
  try:
    collection.insert_one(document)
    result = True
  except Exception:
    result = False
  return result



def read(query):
  '''
  Read single document matching passed query document
  Return JSON document, or given exception on failure
  '''
  try:
    result = collection.find_one(query)
    result = json_util.dumps(result)
  except Exception as e:
    result = e
  return result



def update(old, new):
  '''
  Update document matching 'old' query with 'new' key/value
  Return JSON doc on success, exception on failure
  '''
  try:
    result = collection.update(old, {"$set" : new})
    result = json_util.dumps(result)
  except Exception as e:
    result = e
  return result
    
  

    
def delete(query):
  '''
  Delete document matching given query
  Return JSON result on success, exception on fail
  '''
  try:
    doc = collection.find_one(query)
    result = collection.delete_one(doc)
  except Exception as e:
    result = e
  return result
    
  
# other specialized operations
  
def update_volume(ticker, new_volume):
  '''
  <FINAL 2 B> Update function that specifically matches a Ticker and updates its Volume with a value greater than 0
  '''

  if new_volume <= 0:
    result = "Volume must be greater than zero."
  
  else:
    try:
      result = update({"Ticker": ticker}, {"Volume": new_volume})
    except Exception as e:
      result = e
  
  return result


def delete_ticker(ticker):
  '''
  <FINAL 2 C> Delete function that deletes document with given ticker
  '''
  try:
    result = delete({"Ticker": ticker})
  except Exception as e:
    result = e
  
  return result
  

  
def fifty_day_count(low, high):
  '''
  <FINAL 3 A i> find and count all documents with a 50-day simple moving average within the given range (low, high)
  '''
  try:
    docs = collection.find({"50-Day Simple Moving Average" : {"$gt" : low, "$lt" : high } })
    result = docs.count()
  except Exception as e:
    result = e
  return result
  
  
def find_by_industry(industry):
  '''
  <FINAL 3 A ii> get list of all Ticker strings in a given industry
  '''
  try:
    docs = collection.find({"Industry" : industry})
    result = docs.distinct("Ticker")
  except Exception as e:
    result = e
  return result
    
    
def outstanding_shares(sector):
  '''
  <FINAL 3 B> find total outstanding shares in a sector, grouped by industry
  '''
  try:
    result = collection.aggregate([
      {"$match": {"Sector": sector} },
      {"$group": {"_id": "$Industry", "Total Shares Outstanding": {"$sum" : "$Shares Outstanding"} } } 
    ])
  except Exception as e:
    result = e
  return result # not sure what is expected output here -- currently if try succeeds, result will be a pymongo cursor
  
 
    
    
    
if __name__ == "__main__":
  
  # 3Ai test
  
  low = 0
  high = 0.5
  print
  print("Count averages in range - low {} to high {} --- total documents found: {}".format(low, high, fifty_day_count(low, high)))
  low = 0.5
  high = 2
  print("Count averages in range - low {} to high {} --- total documents found: {}".format(low, high, fifty_day_count(low, high)))
  print
  
  
  # 3Aii test
  
  industry = "Medical Laboratories & Research"
  print
  print("Ticker names in {} Industry --- {}".format(industry, find_by_industry(industry)))
  print
  
  
  # 3B test
  
  sector = "Healthcare"
  print
  print("Total outstanding shares by industry in sector {} ---\n".format(sector))
  cursor = outstanding_shares(sector)
  for doc in cursor:
    print(doc)
  print
  
  
  
  
  
  # test from previous part of project - result shown as screenshot in final document
  
  '''
  # values for testing
  insert_test = {"key" : "value"}
  ticker = "A"
  volume = 123456789
  ticker2 = "BRLI"

  
  
  # basic insert() test
  print
  print("INSERT {} into {} collection in {} database\n  --- {}".format(insert_test, collection_name, db_name, insert(insert_test)))
  print
  print("READ {} from {} collection in {} database\n  --- {}".format(insert_test, collection_name, db_name, read(insert_test)))
  print

  # basic update_volume() test
  print
  print("UPDATE Ticker {} with new Volume {} in {} collection in {} database\n  --- {}".format(ticker, volume, collection_name, db_name, update_volume(ticker, volume)))
  print
  print("READ {} from {} collection in {} database\n  --- {}".format({"Ticker":ticker}, collection_name, db_name, read({"Ticker":ticker})))
  print
  
  # basic delete_ticker test
  print
  print("DELETE {} from {} collection in {} database\n  --- {}".format({"Ticker":ticker2}, collection_name, db_name, delete_ticker(ticker2)))
  print
  print("READ {} from {} collection in {} database\n  --- {}".format({"Ticker":ticker2}, collection_name, db_name, read({"Ticker":ticker2})))
  print
  '''
    
      