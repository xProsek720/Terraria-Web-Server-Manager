from flask import *
import math
import os

###
# TU WSZYSTKO DZIEJE SIĘ SERVERSIDE AŁĆ XD
# ###

inf = math.inf

app = Flask(__name__)
app.secret_key = str(os.urandom(24)).encode("utf-8")
funcCounter = 0
import time


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

import subprocess
@app.route('/', methods = ["GET", "POST"])
def hello():
    cmd = "sudo systemctl status terraria | grep Active:*"
    status_serv = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    session["kalkulacja"] = status_serv.stdout.decode("utf-8").lstrip(" ").lstrip("Active:").split(" ")[1]
    return render_template('index.htm', calc = session['kalkulacja'])

# for i in range(10):
#     funcGen(i, app, i)
# else:
#     funcCounter = i
#
# funcCounter += 1
# funcGen2("+", app, funcCounter)
#
# funcCounter += 1
# funcGen2("-", app, funcCounter)
#
# funcCounter += 1
# funcGen3("*", app, funcCounter)
#
# funcCounter += 1
# funcGen3("/", app, funcCounter, "d")
#
# funcCounter += 1
# funcGen2("(", app, funcCounter)
#
# funcCounter += 1
# funcGen2(")", app, funcCounter)
#
# funcCounter += 1
# funcGen3(".", app, funcCounter, "dot")
#
# @app.route('/e', methods = ["GET", "POST"])
# def hello13():
#     try:
#         if (session['kalkulacja'].startswith("0")):
#             session['kalkulacja'] = session['kalkulacja'].lstrip("0")
#             session["kalkulacja"] = str(eval(session['kalkulacja']))
#         else:
#             session['kalkulacja'] = str(eval(session['kalkulacja']))
#     except SyntaxError:
#         session['kalkulacja'] = '0'
#         print("SYNTAX ERR IN ONE SESSION")
#     except ZeroDivisionError:
#         session['kalkulacja'] = 'inf'
#     except NameError:
#         session['kalkulacja'] = '0'
#     except TypeError:
#         session['kalkulacja'] = '0'
#     except KeyError:
#         session["kalkulacja"] = "0"
#         return render_template('index.htm', calc = session['kalkulacja'])
#     return render_template('index.htm', calc = session['kalkulacja'])
# @app.route('/c', methods = ["GET", "POST"])
# def hello37():
#     if len(session['kalkulacja']) == 1:
#         session['kalkulacja'] = '0'
#     else:
#         session["kalkulacja"] = session['kalkulacja'][0:-1]
#
#    # print(session['kalkulacja'])
#
#     return render_template('index.htm', calc = session['kalkulacja'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
