from Utilities.Config.DBConfig import DbConfig

class DataAccess(DbConfig):
    def __init__(self):
        super(DataAccess, self).__init__()
    def getInstance(self):
        return self.mydb
