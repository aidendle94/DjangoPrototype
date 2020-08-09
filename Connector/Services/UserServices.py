
from Connector.DataAccess import DataAccess
from Model.User import User
from Utilities.EncryptionUtil import EncryptionUtil


class Services(DataAccess):
    def __init__(self):
        super(Services, self).__init__()
        self.Query= None
        self.Cursor = self.getInstance().cursor()
    def createUser(self,User:User):
        values = (User.password,User.firstname,User.lastname,User.username,User.profile)
        self.Query = "INSERT INTO User.User(Password,FirstName,LastName,UserName,Profile) VALUES (%s,%s,%s,%s,%s);"
        self.Cursor.execute(self.Query, values)
        self.mydb.commit()
        return "User Created"
    def getUser(self,InputUsername:str):
        self.Query = ("Select Password,FirstName,LastName,Profile  FROM User.User Where username = %s")
        self.Cursor.execute(self.Query, (InputUsername,))
        result =self.Cursor.fetchone()
        print(result)
        return result
    def validatePassword(self,InPutUsername:str,Password:str):
        EncryptionUtility = EncryptionUtil()
        User = self.getUser(InPutUsername)
        UserPassword = bytes(User[0])
        result = EncryptionUtility.ValidatePassword(hash=UserPassword,password=Password)
        return result











