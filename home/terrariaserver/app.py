from flask import *
import math
import os
import subprocess
import time


app = Flask(__name__)
app.secret_key = str(os.urandom(24)).encode("utf-8")


@app.route('/(', methods = ["GET", "POST"])
def funcCounter():
    cmd = "sudo systemctl status terraria | grep Active:*"
    status_serv = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    os.system("sudo systemctl start terraria")
    session["kalkulacja"] = status_serv.stdout.decode("utf-8").lstrip(" ").lstrip("Active:").split(" ")[1]

    print("ON")
    return render_template('index.htm', calc = session['kalkulacja'])


@app.route('/)', methods = ["GET", "POST"])
def funcCounter1():
    cmd = "sudo systemctl status terraria | grep Active:*"
    status_serv = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    os.system("sudo systemctl stop terraria")
    session["kalkulacja"] = status_serv.stdout.decode("utf-8").lstrip(" ").lstrip("Active:").split(" ")[1]

    print("OFF")
    return render_template('index.htm', calc = session['kalkulacja'])


@app.route('/', methods = ["GET", "POST"])
def hello():
    cmd = "sudo systemctl status terraria | grep Active:*"
    status_serv = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    session["kalkulacja"] = status_serv.stdout.decode("utf-8").lstrip(" ").lstrip("Active:").split(" ")[1]
    return render_template('index.htm', calc = session['kalkulacja'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
