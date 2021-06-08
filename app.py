import json
import requests
from flask import render_template, Blueprint
from flask import Flask, redirect, url_for, request
import os

#Create App
app = Flask(__name__)

#Create Routes
@app.route('/',  methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        query = request.form.get('query')
        response = requests.get(f'https://restcountries.eu/rest/v2/name/{query}')
        
        if query == '':
            return render_template('index.html', searchresults='Search Result returned 0 results. Please enter a valid entry.')
        else:
            json_response = response.json()
            try:
                json_response['status']
                return render_template('index.html', searchresults=f"Search Result for '{query}' returned 0 results. Please enter a valid entry.")
            except:
                json_response = [json_response[i] for i in range(len(json_response))]
                length = len(json_response)
                if length == 1:
                    message = f"Showing {length} Result for '{query}':"

                else:
                    message = f"Showing {length} Results for '{query}':"
                
                return render_template('index.html', results=json_response, searchresults= message) 

    return render_template('index.html')

@app.route('/countryinfo')
def countryinfo():
    return render_template('countryinfo.html', country_name='')

if __name__ == '__main__':
    app.run(debug=True)