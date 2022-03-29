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
        return abort_503()

    if path == LOGIN_PATH and login(request):
        return abort_503()

    my_data = request.get_data()
    if (request.method == 'POST' or request.method == 'PUT') and detect_scraping(sender_ip, path):
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


@app.route('/api/Cards/', methods=['POST', 'GET'])
def carding():
    sender_ip = request.remote_addr
    print("route to login")
    raw_data = request.get_data(as_text=True)
    print(raw_data)
    payload_array = raw_data.split("&")
    full_name = (payload_array[0].split("="))[1].replace("%40", "@")
    card_num = int((payload_array[1].split("="))[1])
    exp_month = (payload_array[2].split("="))[1]
    exp_year = (payload_array[3].split("="))[1]
    print(full_name + "  ::  " + exp_month + "  ::  " + exp_year)
    print(card_num)
    payload = {'fullName': full_name, 'cardNum': card_num, 'expMonth': exp_month,
               'expYear': exp_year}
    return requests.post(f'{SITE_NAME}/api/Cards/', payload).content


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
