from flask import Flask, request
app = Flask('app')

from replit import db
from html_sanitizer import Sanitizer

from pages import *

sanitizer = Sanitizer()

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
   if request.method == 'POST':
      handle = request.form['handle']
      pfp = request.form['pfp']
      postimg = request.form['img']
      postcaption = request.form['caption']
     
      if postimg == "" or postimg == None :
        db["feed"] = "<b style='display: flex;'><img src='" + pfp + "' width='50' height='50'/>" + sanitizer.sanitize(handle) + "</b><hr/>"+ postcaption + "<hr/><br/>" + db["feed"]
        return 'ooga booga'
      else :
        db["feed"] = "<b style='display: flex;'><img src='" + pfp + "' width='50' height='50'/>" + sanitizer.sanitize(handle) + "</b><hr/><img src='" + postimg + "'/>"+ postcaption + "<hr/><br/>" + db["feed"]
   else:
      return "You're not supposed to be here..."


app.run(host='0.0.0.0', port=8080)