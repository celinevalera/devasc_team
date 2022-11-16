from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Heart(db.Document):
    heart_id = db.IntField(required=True, unique=True)
    date = db.DateField(required=True, unique=False)
    heart_rate= db.IntField(required=True, unique=False)

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self,password):
        return check_password_hash(self.password, password)
