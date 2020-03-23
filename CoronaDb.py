import pymongo
from RivmData import RivmData, RivmDataEntries

class CoronaDb:
    def __init__(self):
        self.db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.db_client["hoeveelcoronagevallen_nl"]
        self.db_rivm = self.db["rivm"]
    
    def add_data(self, rivmData: RivmData):
        self.db_rivm.insert_one(rivmData.toDict())
    
    def get_data(self) -> RivmData:
        doc = self.db_rivm.find({}).sort([(RivmDataEntries.unix_time, pymongo.DESCENDING)])
        for x in doc:
            return RivmData.fromDict(x)
        return None