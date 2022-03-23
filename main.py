import time
import json
from requests import post, get

from detector import *
from fake_responses import *
import requests
from flask import Flask, request, Response

app = Flask('__main__')
SITE_NAME = "http://127.0.0.1:3000/"


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

    return get(f'{SITE_NAME}{path}').content


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
    # if detect_brute_force_password(extract_email, extract_password, sender_ip):  # extract ip and time
    #   return hold_session(requests.Session())

    return requests.post(f'{SITE_NAME}/api/Cards/', payload).content


# post data for juice shop http://localhost:5000/#/login
@app.route('/rest/user/login', methods=['POST', 'GET'])
def login():
    sender_ip = request.remote_addr
    print("route to login")
    raw_data = request.get_data(as_text=True)
    payload_array = raw_data.split("&")
    email = (payload_array[0].split("="))[1].replace("%40", "@")
    password = (payload_array[1].split("="))[1]
    print(email + "  ::  " + password)
    payload = {'email': email, 'password': password}
    if detect_brute_force_password(email, password, sender_ip):  # extract ip and time
        return abort_503()

    return requests.post(f'{SITE_NAME}/rest/user/login', payload).content


app.run(debug=True)
