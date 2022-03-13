import time
from requests import post

from detector import detect_brute_force_password
from fake_responses import *
import requests
from flask import Flask, request, Response

app = Flask('__main__')
SITE_NAME = 'https://hack-yourself-first.com/'


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

    resp = requests.request(
        method=request.method,
        url=SITE_NAME + path)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)

    return response


@app.route('/Account/Login',methods=['POST', 'GET'])
def login():
    raw_data = request.get_data(as_text=True)
    payload_array = raw_data.split("&")
    email = (payload_array[0].split("="))[1].replace("%40","@")
    password = (payload_array[1].split("="))[1]
    # input validation
    if (payload_array[0].split("="))[0] != "Email" or (payload_array[1].split("="))[0] != "Password":
        return 'Invalid Parameters in Your Json'
    if detect_brute_force_password(email, password):    # extract ip
        return abort_503()
    payload = {'Email': email, 'Password': password}
    return post(f'{SITE_NAME}/Account/Login',data=payload).content


app.run(debug=True)
