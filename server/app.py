#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response # type: ignore

app = Flask(__name__)

@app.before_request
def before_request():
     g.path = os.path.abspath(os.getcwd())
     

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    reponse_body = f'''<h1>The host for this page is {host}</h1>
             <h2>The app name is {appname}</h2>
             <h3> The Path of this appliction on the users's machine is {g.path}</h3>
             <h4>The path of this file is {__file__}</h4>'''
             
    status_header = 200
    header = {}
    
    return make_response(reponse_body, status_header, header)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
