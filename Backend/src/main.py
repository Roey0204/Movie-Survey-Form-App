'''
Author: Roey
Description: This module aims to facilitate the creation of custom endpoints, 
demonstrating a proof of concept for showcasing REST API functionality in backend services..

'''
from flask import Flask
from flask_restful import Api
import sys
from flask_sqlalchemy import SQLAlchemy
sys.path.append('..')

from model.model import db
from controller.resources import Movie

import os

# Get the current working directory
current_dir = os.getcwd()

# Get the parent directory (up one layer)
parent_dir = os.path.dirname(current_dir)

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{parent_dir}/database/database.db'

db.init_app(app)

api.add_resource(Movie, "/movie/<int:movie_id>")

if __name__ == "__main__":
    app.run(debug=True)
