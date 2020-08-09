from flask import Flask, logging,jsonify

from Model.User import User

app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Hello World!'
@app.route('/user/createuser/<username>/password/<password>/firstname/<firstname>/lastname/<lastname>/profile/<profile>',methods=['POST'])
def userCreateUser(username,password,firstname,lastname,profile):
    user = User()
    user.createUserObject(firstname=firstname,lastname=lastname,username=username,password=password,profile=profile)
    return jsonify(firstname = firstname,lastname=lastname,profile=profile)

if __name__ == '__main__':
    app.run()
