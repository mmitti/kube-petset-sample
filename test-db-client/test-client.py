from flask import Flask, render_template, request, redirect, url_for
import sys
import requests as req
import json
import os
from socket import gethostname

app = Flask(__name__)
api = ""
api_pod = ""
@app.route('/')
def index():
    r = req.get('http://'+api+"/info")
    return redirect(url_for('room', name=r.json()['current_host'], _external=True))

@app.route('/room/<name>')
def room(name):
    r = req.get('http://'+name+'.'+api_pod+"/get")
    r2 = req.get('http://'+name+'.'+api_pod+"/info")
    return render_template('index.html', view_host=gethostname() data=r.json(),
        info=r2.json(), url=url_for("post", _external=True), room=name)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        text = request.form['text']
        room = request.form['room']
        req.post('http://'+room+'.'+api_pod+"/add", data=json.dumps({"text":text, "host":gethostname()}))
        return redirect(url_for('room', name=room, _external=True))
    else:
        return redirect(url_for('index' , _external=True))

if __name__ == '__main__':
    api = os.environ["API"]
    api_pod = os.environ["API_POD"]
    app.run(host='0.0.0.0')
