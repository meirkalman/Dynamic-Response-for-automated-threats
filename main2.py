# proxy for hack-yourself-first site

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
    # bank of responses:
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

    resp = requests.request(
        method=request.method,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        url=SITE_NAME + path,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    # issue: files in response are linked straight to hack-yourself site so if you press a button you will lose the
    # connection to our  proxy...
    # solution: let's replace the href's to our proxy (replace protocol + domain)
    my_data = resp.content
    my_data1 = my_data.replace(b'https://hack-yourself-first.com', b'http://127.0.0.1:5000')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(my_data1, resp.status_code, headers)
    return response


COUNTER = 0


# post data for juice shop http://localhost:5000/#/login
def login(request):
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
