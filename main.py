import time
from requests import post, get

from detector import detect_brute_force_password, detect_dos_attack
from fake_responses import *
import requests
from flask import Flask, request, Response

app = Flask('__main__')
SITE_NAME = "http://127.0.0.1:3000/"


def detect_attack():
    return True


@app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
def proxy(path):
    # s = requests.session()
    # if detect_attack():
    # option 1:
    # abort_503()
    # option 2
    # return empty_response()
    # option 3:
    # sleep_abort()
    # option 4:
    # return fake_response()
    # option 5:
    # return hold_session(s)

    sender_ip = request.remote_addr
    if detect_dos_attack(sender_ip):
        return abort_503()

    # return get(f'{SITE_NAME}{path}').content
    resp = requests.request(
        method=request.method,
        url=SITE_NAME + path,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


# post data for juice shop http://localhost:5000/#/login
@app.route('/login',methods=['POST', 'GET'])
def login():
    raw_data = request.get_data(as_text=True)
    print(raw_data)
    payload_array = raw_data.split("&")
    extract_email = (payload_array[0].split("="))[1].replace("%40","@")
    extract_password = (payload_array[1].split("="))[1]
    payload = {'email': extract_email, 'password': extract_password}
   # if detect_brute_force_password(extract_email, extract_password, sender_ip):  # extract ip and time
       # return sleep_abort()

    return post(f'{SITE_NAME}/#/login',data=payload).content




"""
#post data for hack-yourself-first.com
@app.route('/Account/Login',methods=['POST', 'GET'])
def login():
    sender_ip = request.remote_addr
    raw_data = request.get_data(as_text=True)
    payload_array = raw_data.split("&")
    email = (payload_array[0].split("="))[1].replace("%40","@")
    password = (payload_array[1].split("="))[1]
    # input validation
    if (payload_array[0].split("="))[0] != "Email" or (payload_array[1].split("="))[0] != "Password":
        return 'Invalid Parameters in Your Json'

    if detect_brute_force_password(email, password, sender_ip):    # extract ip and time
        return abort_503()
    payload = {'Email': email, 'Password': password}
    return post(f'{SITE_NAME}/Account/Login',data=payload).content

"""

app.run(debug=True)
