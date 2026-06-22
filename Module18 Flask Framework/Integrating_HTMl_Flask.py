# Integrating the streamlit in the flask web framework takes place as with the same revious code as: 

from flask import Flask, render_template
'''
It creates an instance of the flask
which will be your WSGI application 
''' 

app = Flask(__name__) 

@app.route("/")
def welcome(): 
    return "<html><H1>Welcome to the Flask Course. This should be an amazing course<H1><html>"  

@app.route("/index") 
def index(): 
    return render_template("index1.html") 

@app.route('/about') 
def about(): 
    return render_template('about.html')



if __name__=="__main__": 
    app.run(debug = True)  

# Hence html has been properly integrated in this flask python code. 


