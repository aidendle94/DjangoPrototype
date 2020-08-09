import bcrypt


class EncryptionUtil:

    def __init__(self):
        pass
    def EncryptPassword(self,inputpass):
        salted = bcrypt.hashpw(bytes(inputpass,'utf-8'), bcrypt.gensalt())
        print(salted)
        return salted

    def ValidatePassword(self, hash,password):
        password = bytes(password,'utf-8')
        if bcrypt.checkpw(password,hash):
            return True
        else:
            return False

