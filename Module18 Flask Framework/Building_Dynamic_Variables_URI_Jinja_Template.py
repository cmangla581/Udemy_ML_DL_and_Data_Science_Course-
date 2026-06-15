
from flask import Flask, render_template, request
'''
It creates an instance of the flask
which will be your WSGI application 
''' 

'''
Jinja 2 Template Engine:  

{{ }} expressions to print the output in html 
{%..%}  ondition , for loops 
{#....#}  for comments 
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

@app.route('/submit', methods = ['GET', 'POST']) 
def form(): 
    if request.method == 'POST':
        name = request.method['name']
        return f'Hello {name}!'
    return render_template("form.html") 

## Variable Rule 
@app.route('/successres/<int:score>') 
def success(score): 
    res = "" 
    if score >= 50:
        res = "PASS"
    else: 
        res = "FAIL" 

    return render_template('result.html') 

@app.route('/fail/<int:score>') 
def fail(score): 

    return render_template('result.html', results = score) 




if __name__=="__main__": 
    app.run(debug = True)  