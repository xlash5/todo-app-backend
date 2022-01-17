from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    full_name = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __init__(self, username, password, full_name, mail):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.mail = mail

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'mail': self.mail,
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
