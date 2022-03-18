from flask import Flask, request, jsonify, make_response
app = Flask('app')

from replit import db
from html_sanitizer import Sanitizer

from pages import *

sanitizer = Sanitizer()

from threading import Thread
import random
import time
import requests
import logging

@app.route('/')
def route1 ():
  return html1

@app.route('/feed')
def route0 ():
  return db["feed"]

@app.route('/connect', methods = ['POST'])
def route2 ():
  handle = request.form['handle']
  return "success"

@app.route('/post',methods = ['POST', 'GET'])
def login():
   req = request.get_json()
   
   if request.method == 'POST':
      print(req)
      handle = req["handle"]
      pfp = req["pfp"]
      postimg = req["img"]
      postcaption = req["postcaption"]
      postcaption = sanitizer.sanitize(postcaption)

      if postimg == "" or postimg == None :
        db["feed"] = "<b style='display: flex;'><img src='" + pfp + "' width='50' height='50'/>" + sanitizer.sanitize(handle) + "</b><hr/>"+ postcaption + "<hr/><br/>" + db["feed"]
        return 'ooga booga'
      else :
        db["feed"] = "<b style='display: flex;'><img src='" + pfp + "' width='50' height='50'/>" + sanitizer.sanitize(handle) + "</b><hr/><img src='" + postimg + "'/>"+ postcaption + "<hr/><br/>" + db["feed"]
   else:
      return "You're not supposed to be here..."

def run () :
  app.run(host='0.0.0.0', port=8080)

def ping(target, debug):
    while(True):
        r = requests.get(target)
        if(debug == True):
            print(r.status_code)
        time.sleep(random.randint(30,60))
      
def awake(target, debug=False):  
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True  
    t = Thread(target=run)
    r = Thread(target=ping, args=(target,debug,))
    t.start()
    r.start()
  
awake("https://3COM-PALM-3.codesalvageon.repl.co", True)