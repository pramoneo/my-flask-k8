# flask_web/app.py

from flask import Flask, render_template, url_for, request
app = Flask(__name__, static_folder='static')

import socket, os, platform

myHostName = socket.gethostname()
myIP   = socket.gethostbyname(myHostName)
myPid = os.getpid()
myKernel = os.uname()
myUid = os.getuid()
myk8ns = os.getenv('NAMESPACE')
myk8host = os.getenv('K8HOST')

@app.route('/')
def hello_world():
    return render_template('index.html', message=myHostName, IP=myIP, PID=myPid, KERNEL=myKernel, UID=myUid, K8NS=myk8ns, KHOST=myk8host)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

