import bcrypt


class EncryptionUtil():

    def __init__(self, password):
        self.password = bytes(password, 'utf-8')
        self.salted = None

    def EncryptPassword(self):
        self.salted = bcrypt.hashpw(self.password, bcrypt.gensalt())
        return self.salted

    def ValidatePassword(self, hash):
        hash = bytes(hash, 'utf-8')

        if bcrypt.checkpw(hash, self.salted):
            return "Sccess"
        else:
            return "fail"
test = EncryptionUtil('password')
test.EncryptPassword()
print(type(test.salted))
