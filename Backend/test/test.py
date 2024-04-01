'''
Description : REST API Testing use case
'''
import requests

class ApiTesting:
    def __init__(self):      
        self.BASE = "http://127.0.0.1:5000/"
               
    def receive(self,id:int):
        response = requests.get(self.BASE + f"movie/{id}")
        return response.json()
        
    def create(self,id:int,data:dict):
        response = requests.put(self.BASE + f"movie/{id}",data)
        return response.json()
        
    def update(self,id:int,data):
        response = requests.patch(self.BASE + f"movie/{id}",data)
        return response.json()
    
    def delete(self,id:int):
        response = requests.delete(self.BASE+f"movie/{id}")
        return response
        
if __name__ == "__main__":
    test = ApiTesting()
    
    data = {
        "name":"Kid",
        "views":1000,
        "likes":200       
    }
    
    test.create(2,data)
    
    test.receive(2)
    
    test.update(2,data)
    
    test.delete(data)