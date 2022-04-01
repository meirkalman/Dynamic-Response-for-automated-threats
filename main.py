# proxy for OWASP juice-shop app

import binascii
import time
import json
from requests import post, get

from detector import *
from fake_responses import *
import requests
from flask import Flask, request, Response

app = Flask('__main__')
SITE_NAME = "http://127.0.0.1:3000/"
LOGIN_PATH = 'rest/user/login'


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
        # issue: response of fake html is not possible because client sent ajax request so
        # it will not re-render the page... print only "[Object object]"...
        return abort_503()

    if path == LOGIN_PATH and login(request):
        return abort_503()

    my_data = request.get_data()
    if (request.method == 'POST' or request.method == 'PUT') and detect_scraping(sender_ip, path):
        # issue: we want to return error message but the server return valid payload
        # solution: we changed the code in server to return our desired error message and here
        # we send a flag to server to do it
        # better solution (did not implemented here): hold the error message here in proxy
        # and replace the response that we get from server accordingly (in line 68+-)
        my_data = request.get_json()
        my_data["nudnik"] = True
        json_string = json.dumps(my_data).encode()
        my_data = json_string

    resp = requests.request(
        method=request.method,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        url=SITE_NAME + path,
        data=my_data,
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


# post data for juice shop http://localhost:5000/#/login
def login(request):
    sender_ip = request.remote_addr
    raw_data = request.get_json()
    email = raw_data["email"]
    password = raw_data["password"]
    print(email + "  ::  " + password)
    if detect_brute_force_password(email, password, sender_ip):  # extract ip and time
        return True
    return False


app.run(debug=True)
