
import random
import os
from bson.json_util import dumps

var_mongodb = os.environ.get('MONGODB')
var_collection = os.environ.get('MONGOCOLLECTION')

def get_companies(client, number = 0):
    mydb = client[var_mongodb]
    collection = mydb[var_collection]
    if (number == 0):
        amount = int(random.random()*100)        
        query={"numEmps":{"$gt":amount}}
    else:
        query={"numEmps":{"$gt":number}}
    docs = collection.find(query)
    
    return docs
