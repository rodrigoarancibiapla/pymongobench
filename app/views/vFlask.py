import flask as webFW 
from app import appFlask as myapp
from app.models import DBPyMongo
from bson.json_util import dumps


dbObj=None

@myapp.route("/companies/",defaults={'employees': 0},methods = ['GET'])
@myapp.route("/companies/<int:employees>",methods = ['GET'])
def companies(employees):  
    global dbObj
    if dbObj==None:
        dbObj = DBPyMongo.DBPyMongo()  

    companies_cursor = dbObj.get_companies(employees)
    companies=list(companies_cursor)[:100]    
    
    return webFW.Response(dumps(companies), status=200)

