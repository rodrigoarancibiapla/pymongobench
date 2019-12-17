import quart as webFW 
from app import appQuart as myapp
from app.models import DBMotorIO
from bson.json_util import dumps


dbObj=None

@myapp.route("/companies/",defaults={'employees': 0},methods = ['GET'])
@myapp.route("/companies/<int:employees>", methods = ['GET'])
async def companies(employees):
    global dbObj
    if dbObj==None:
        dbObj = DBMotorIO.DBMotorIO()  
    
    companies = dbObj.get_companies(employees)
    mylist= (await companies.to_list(length=100))
    return webFW.Response(dumps(mylist), status=200)


