from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_id = db.Column(db.String(30), primary_key=True, unique=True)
    user_name = db.Column(db.String(30))
    profile_url = db.Column(db.String(100))
    created = db.Column(db.DateTime)

    def __init__(self, user_id, user_name, profile_url):
        self.user_id = user_id
        self.user_name = user_name
        self.profile_url = profile_url
        self.created = datetime.now()

    def __repr__(self):
        return 'user_id : %s, user_name : %s, profile_url : %s' % (self.user_id, self.user_name, self.profile_url)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
