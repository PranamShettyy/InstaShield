from flask import Flask, render_template , request
import filter_img as fi
import os 
import subprocess
import setproxy as sp

app = Flask(__name__,template_folder="templates" )
flag=0
process = None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def startproxy():
    if request.method == 'POST':
        rest_type = request.form['proxyOptions']
        fi.getval(rest_type)
        sp.set_proxy(enable=True, proxy_server="127.0.0.1:8080")
        global process
        if process is None or process.poll() is not None:  # Check if the subprocess is not running
            process=subprocess.Popen(['mitmdump','-s','proxy.py'])
    return render_template('index1.html')

@app.route('/stopro')
def stopro():
    sp.set_proxy(enable=False, proxy_server="127.0.0.1:8080")
    global process
    if process is not None and process.poll() is None:  # Check if the subprocess is running
        process.terminate() 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
