'''
This module serve as Controller module to handle the action and configuration setting for REST API.
'''
from flask_restful import Resource, reqparse, abort, fields, marshal_with
import sys
sys.path.append('..')
from model.model import db, MovieModel

class Parse:
    def __init__(self):
        
        '''
        Ensures that the incoming data must include "name", "scores", and "age" fields, and 
        these fields must adhere to the specified types and constraint
        '''
        
        self.movie_put_args = reqparse.RequestParser()
        self.movie_put_args.add_argument("name", type=str, help="Name of the movie is required", required=True)
        self.movie_put_args.add_argument("scores", type=int, help="scores of the movie", required=True)
        self.movie_put_args.add_argument("age", type=int, help="age on the movie", required=True)
        self.movie_put_args.add_argument("comment", type=str, help="comment of the movie is required", required=True)

        self.movie_update_args = reqparse.RequestParser()
        self.movie_update_args.add_argument("name", type=str, help="Name of the movie is required")
        self.movie_update_args.add_argument("scores", type=int, help="scores of the movie")
        self.movie_update_args.add_argument("age", type=int, help="age on the movie")
        self.movie_update_args.add_argument("comment", type=str, help="comment of the movie is required")
        
        '''
         Used with the marshal_with() decorator or the marshal() function provided by Flask-RESTful to 
         automatically format and serialize response data according to these field definitions
        '''
         
        self.resource_fields = {
            'id': fields.Integer,
            'name': fields.String,
            'scores': fields.Integer,
            'age': fields.Integer,
            "comment":fields.String
        }

class Movie(Resource):
    '''
    Rest API Controller to demonstrate CRUD
    Create, Received, Update, Delete
    '''
    @marshal_with(Parse().resource_fields)
    def get(self, movie_id:int):
        result = MovieModel.query.filter_by(id=movie_id).first()
        if not result:
            abort(404, message="Could not find movie with that id")
        return result

    @marshal_with(Parse().resource_fields)
    def put(self, movie_id:int):
        args = Parse().movie_put_args.parse_args()
        check = MovieModel.query.count() +1
        result = MovieModel.query.filter_by(id=check).first()
        if result:
            abort(409, message="Movie id taken...")
        movie = MovieModel(id=check, name=args['name'], scores=args['scores'], age=args['age'],comment=args['comment'])
        db.session.add(movie)
        db.session.commit()
        return movie, 201

    @marshal_with(Parse().resource_fields)
    def patch(self, movie_id:int):
        args = Parse().movie_update_args.parse_args()
        result = MovieModel.query.filter_by(id=movie_id).first()
        if not result:
            abort(404, message="Movie doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['scores']:
            result.scores = args['scores']
        if args['age']:
            result.age = args['age']
        if args['comment']:
            result.age = args['comment']

        db.session.commit()

        return result

    def delete(self, movie_id:int):
        movie = MovieModel.query.get(movie_id)
        if not movie:
            abort(404,message="Could not find movie...")
        else:
            db.session.delete(movie)
            db.session.commit()

        return 204
