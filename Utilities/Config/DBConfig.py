import mysql.connector


class DbConfig:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="testuser",
            passwd="megaman1",
            database="Menu",
            auth_plugin='mysql_native_password'
        )
    def get(self):
        return self.mydb