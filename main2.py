# for hack-yourself-first site

import binascii
import time
import json
from requests import post, get

from detector import *
from fake_responses import abort_503
import requests
from flask import Flask, request, Response, render_template

app = Flask('__main__')
SITE_NAME = "http://hack-yourself-first.com/"
LOGIN_PATH = 'Account/Login'


@app.route('/', defaults={'path': ''}, methods=['POST', 'GET', 'PUT'])
@app.route('/<path:path>', methods=['POST', 'GET', 'PUT', 'DELETE'])
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
    if detect_dos_attack(sender_ip, path):
        return fake_response()

    if path == LOGIN_PATH and request.method == 'POST' and login(request):
        return fake_response()

    my_data = request.get_data()

    """
    if (request.method == 'POST' or request.method == 'PUT') and detect_scraping(sender_ip, path):
        my_data = request.get_json()
        my_data["nudnik"] = True

        json_string = json.dumps(my_data).encode()
        my_data = json_string
    """
    resp = requests.request(
        method=request.method,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        url=SITE_NAME + path,
        data=my_data,
        cookies=request.cookies,
        allow_redirects=False)

    my_data2 = resp.content
    my_data3 = my_data2.replace(b'https://hack-yourself-first.com', b'http://127.0.0.1:5000')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(my_data3, resp.status_code, headers)
    return response


COUNTER = 0


# post data for juice shop http://localhost:5000/#/login
def login(request):
    """
    sender_ip = request.remote_addr
    raw_data = request.get_json()
    email = raw_data["Email"]
    password = raw_data["Password"]
    print(email + "  ::  " + password)
    if detect_brute_force_password(email, password, sender_ip):  # extract ip and time
        return True
    """
    # TODO: improve logic as in main ...
    global COUNTER
    COUNTER = COUNTER + 1
    if COUNTER >= 3:
        return True
    return False


def fake_response():
    index = "FAKE_hack_yourself_first.html"
    return render_template(index)


app.run(debug=True)
