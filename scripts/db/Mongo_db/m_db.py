import pymongo 

class mongo_db:
    def __init__(self, connection_string):
        self.connectionString = connection_string
        self.myclient = pymongo.MongoClient(self.connectionString)
        self.db = self.myclient["Library_management_System"]
        try:
            self.myclient.server_info()
            print("Connection started successfully")
            if self.myclient and self.db is not None:
                print("Connection established successfully")
            else:
                print("Exiting program due to connection failure")
        except pymongo.errors.ConnectionFailure as e:
            print(e)
