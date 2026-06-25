# here, we will be creating a simple web app skeleton  
from flask import Flask   
'''
It creates an instance of the flask
which will be your WSGI application 
''' 

app = Flask(__name__) 

@app.route("/")
def welcome(): 
    return "Welcome to the Flask Course. This should be an amazing course"  

@app.route("/index") 
def index(): 
    return "Welcome to the index page"



if __name__=="__main__": 
    app.run(debug = True) 

# Here as we can see that we have clearly come to know the functions of the web page applications properly 
