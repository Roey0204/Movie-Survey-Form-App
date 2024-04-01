'''
Model Of the database

'''
from flask_sqlalchemy import SQLAlchemy

db    = SQLAlchemy()

class MovieModel(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Movie(name = {self.name}, views = {self.views}, likes = {self.likes})"