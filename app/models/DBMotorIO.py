import motor.motor_asyncio
import os
import app.models.MDBCompanies as MDBCompanies
from app.models.DBInterface import DBInterface 


class DBMotorIO(DBInterface):
    def __init__(self):
        var_mongouri = os.environ.get('MONGOURI')
        self.client =  motor.motor_asyncio.AsyncIOMotorClient(var_mongouri)

    def get_companies(self, number):
        mydoc= MDBCompanies.get_companies(self.client, number)
        return mydoc

        



