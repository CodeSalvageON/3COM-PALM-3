from flask import Flask, request
app = Flask('app')

from replit import db

from pages import *

@app.route('/')
def route1 ():
  return html1

@app.route('/connect', methods = ['POST'])
def route2 ():
  handle = request.form['handle']
  return "success"

app.run(host='0.0.0.0', port=8080)