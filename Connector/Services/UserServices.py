from Connector.DataAccess import DataAccess


class Services(DataAccess):
    def __init__(self):
        super(Services, self).__init__()
    def createUser(self,User):
        User()