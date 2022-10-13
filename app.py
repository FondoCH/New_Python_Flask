from email.policy import default
from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape

app = Flask (__name__)



@app.route('/')
def index():
    return "Hello World"


@app.route('/home')
def home():
    return "This is the home page for this project"

@app.route('/projects/')
def projects():
    return "<h1>The projects page.</h1><p>Here, we are going to take you through a whole list of all active projects that we are carrying!</p><p><i>Thank you, and be attentive!</i></p>"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/default', defaults={'params':'Charlessss'})
@app.route('/default/<params>')
def DEFAULT(params):
    return 'The parameter is: ' + params

@app.route('/str-url/<string:str_params>')
def String_Func(str_params):
    return 'The string parameter is: ' + str_params

@app.route('/float-url/<float:float_params>')
def Float_Func(float_params):
    return 'The float parameter is : ' + str(float_params)

@app.route('/path-route/<path:our_path>')
def Path_Func(our_path):
    return 'Our path is: '+ our_path

@app.route('/combine-route/<string:name>/<int:num>')
def Combine_Func(name,num):
    return 'User name is: '+ name + ' and user age is: ' +str(num)


































if __name__ == '__main__':
   app.run(dedug=True)