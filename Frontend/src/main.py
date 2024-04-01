'''
This module just a dummy front end survey form UI just to test the back end services.
'''

from flask import Flask, render_template, request, redirect, url_for
import requests
import os

# Get the current working directory
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)

app = Flask(__name__, template_folder=f'{parent_dir}/templates')

class ApiTesting:
    def __init__(self):      
        self.BASE = "http://127.0.0.1:5000/"
        self.latest_id = 0  # Initialize the latest ID
        
    def receive(self, id: int):
        response = requests.get(self.BASE + f"movie/{id}")
        return response.json()
        
    def create(self,data: dict):
        id = 0
        response = requests.put(self.BASE + f"movie/{id}", json=data)
        return response.json()
        
    def update(self, id: int, data):
        response = requests.patch(self.BASE + f"movie/{id}", json=data)
        return response.json()
    
    def delete(self, id: int):
        response = requests.delete(self.BASE + f"movie/{id}")
        return response

@app.route('/')
def index():
    return render_template('survey_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    movie = request.form['movie']
    scores = int(request.form['score'])
    age = int(request.form['age'])
    comment = request.form['comment']
    
    # Prepare data to send through API
    data = {'name': movie, 'scores': scores, 'age': age, 'comment': comment}

    # Create an instance of the ApiTesting class
    api = ApiTesting()
    
    # Send data through API
    api.create(data)

    # Render the same template again
    return render_template('survey_form.html')

@app.route('/movie/<int:id>')
def movie(id):
    api = ApiTesting()
    movie_data = api.receive(id)
    return f"Movie ID: {id}, Data: {movie_data}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
