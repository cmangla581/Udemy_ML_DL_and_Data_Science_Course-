# Practical example of the Verbs and Get Post which can be shown as:  

'''
Get and Post are the 2 methods used to communicate between the client and the server. They are most commonly used through the 
Python requests libray and are HTTP methods. 
''' 

from flask import Flask, render_template, request
'''
It creates an instance of the flask
which will be your WSGI application 
''' 

app = Flask(__name__) 

@app.route("/")
def welcome(): 
    return "<html><H1>Welcome to the Flask Course. This should be an amazing course<H1><html>"  

@app.route("/index", methods = ['GET']) 
def index(): 
    return render_template("index1.html") 

@app.route('/about') 
def about(): 
    return render_template('about.html') 

@app.route('/form', methods = ['GET', 'POST']) 
def form(): 
    if request.method == 'POST':
        name = request.method['name']
        return f'Hello {name}!'
    return render_template("form.html")



if __name__=="__main__": 
    app.run(debug = True)  
