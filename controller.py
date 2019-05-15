#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
import json
import subprocess
from flask_cors import CORS
from table import table


app = Flask(__name__)
cors = CORS(app)




@app.route('/', methods=['GET', 'POST'])
def script():
    if request.method == 'POST': 
        data = json.loads(request.data)
        #parse json object to get script
        #WHITESPACE needs to be preserved - will it be saved? /t for ex
        script = data['one'] #one key placeholder for script text

        f = open('script.py','w+')
        f.write(script)

        command = 'python3 script.py'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = p.communicate() #we will need to parse the output to allow it to be input into a JSON object
        response_ = {}
        response_['output'] = response
        return jsonify(response_)

@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'GET': 
        first_col = table.table()
        return jsonify({'first':first_col})


