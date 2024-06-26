from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# @app.route('/',methods=['GET'])
# def home():
#     return jsonify({'name':'charles','Age':'18'})

basedir = os.path.abspath(os.path.dirname(__file__)) # check directry

app.config['SQLALACHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'db.sqlite') # connect with Data base with path
app.config['SQLALACHEMY_TRACK_MODIFICATION'] =False # Warning disablity 


db = SQLAlchemy(app) # varable creation by (app)
app.app_contect().push()
ma = Marshmallow(app)

class User(db.Model):
    id = db.Collumn(db.Integer,primary_key = True)
    Name = db.Collumn(db.String(100))
    Contact = db.Collumn(db.Integer, unique= True)


def __init__(self,Name,Contact):
    self.Name = Name
    self.Contact =Contact

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','Name','Contact') # It show tha outside

User_schema = UserSchema()   # You have add mulitible data you will be right this Both code
Users_schema = UserSchema(many=True)

if __name__=='__main__':
    app.run(debug=True,port=5000)