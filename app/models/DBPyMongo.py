import pymongo
import os
import app.models.MDBCompanies as MDBCompanies
from app.models.DBInterface import DBInterface 
from bson.json_util import dumps

class DBPyMongo(DBInterface):
    def __init__(self):
        var_mongouri = os.environ.get('MONGOURI')        
        self.client = pymongo.MongoClient(var_mongouri)        
               
    def get_companies(self, number):
        return MDBCompanies.get_companies(self.client, number)



