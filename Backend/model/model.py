'''
Model Of the database
Database can be generate on this module based on the MovieModel information
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Get the current working directory
current_dir = os.getcwd()

# Get the parent directory (up one layer)
parent_dir = os.path.dirname(current_dir)

db    = SQLAlchemy()

class MovieModel(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Movie(name = {self.name}, views = {self.views}, likes = {self.likes})"
    
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{parent_dir}/database/Movie_Database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app, db

if __name__ == "__main__":
    
    from flask_restful import Api
    from model import create_app

    # Initialize Flask app and SQLAlchemy
    app, db = create_app()
    
    # Create API instance
    api = Api(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
