from Utilities.EncryptionUtil import EncryptionUtil

class User():
    def __init__(self) :
        self.UserID = None
        self.firstname = None
        self.lastname = None
        self.username = None
        self.password = None
        self.profile = None

    def createUserObject(self,firstname,lastname,username,password,profile):
        SALT = EncryptionUtil()
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = SALT.EncryptPassword(password)
        self.profile = profile

