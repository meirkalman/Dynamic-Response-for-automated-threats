import simplejson
import time
from fake_responses import *
import requests
from flask import *
from requests import *


app = Flask('__main__')
SITE_NAME = 'https://hack-yourself-first.com/'


def detect_attack():
    return True


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
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

    return get(f'{SITE_NAME}{path}').content


app.run( debug=True)


"""

@app.route('/Account/Login',methods = ['POST','GET'])
def login():
    payload = {'Email': 'dsfs@gmail.com', 'Password': '12345678'}
    return post(f'{SITE_NAME}/Account/Login',data=payload).content




    
 # if request.method == 'POST':
    password =request.POST.get('Password','')

    email = request.POST.get('Email','')
    payload = {'Email': email, 'Password': password}
"""