from flask import Flask
from flask_restful import Api
from resources.usersearch import UserSearch
from resources.userlist import UserList
from resources.usercrud import UserCrud
from resources.contacts import ContactCreate, ContactSearch
from resources.contacts import ContactCreate, ContactSearch
from database import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    db.create_all()

api.add_resource(UserList, '/us')                         
api.add_resource(UserCrud, '/user/<int:id>')          
api.add_resource(UserSearch, '/user/search/<string:name>')  
api.add_resource(ContactSearch, '/user/<int:user_id>/contacts')
api.add_resource(ContactCreate, '/user/<int:userId>/contact/<int:contactUserId>')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
