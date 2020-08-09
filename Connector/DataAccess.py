from Utilities.Config.DBConfig import DbConfig

class DataAccess(DbConfig):
    def __init__(self):
        super(DataAccess, self).__init__()
    def getInstance(self):
        if self.mydb.is_connected():
            print("Connected")
        else:
            print("No connection")
        return self.mydb
