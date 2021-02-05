from apps import db, app
from models import User, users_share_schema
import datetime
import jwt

class UserControl:

    def __init__(self):
        self.db = db

    def insert(self, model):
        self.db.session.add(model)
        self.db.session.commit()
    
    def create_user(self, username, email, password):
        return User(username, email, password)


    def update(self, new_data, id):
        User.query.filter_by(id=id).update(
            dict(username=new_data.username, email=new_data.email, password=new_data.password))
        self.db.session.commit()
    
    def create_token(self, user):
        payload = {'id': user.id, 'exp': datetime.datetime.utcnow() +
               datetime.timedelta(hours=10)}
        token = jwt.encode(
        payload, app.config['SECRET_KEY'], algorithm="HS256")
        return token
    
    def return_user(self, id):
        user = users_share_schema.dump(User.query.filter_by(id=id))
        return user[0]
        
    
    def return_object(self, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        if email:
            return User.query.filter_by(email=email).first_or_404()
        return User.query.filter_by(username=username).first_or_404()

user_control = UserControl()