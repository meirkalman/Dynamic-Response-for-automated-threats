
import time
from fake_responses import *
import requests
from flask import *
from requests import *


app = Flask('__main__')
SITE_NAME = 'http://localhost:3000/'


def detect_attack():
    return True


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    s = requests.session()
    #if detect_attack():
        # option 1:
        # abort_503()
        # option 2
        # return empty_response()
        # option 3:
        # sleep_abort()
        # option 4:
        # return fake_response()
        # option 5:
        #return hold_session(s)

    return get(f'{SITE_NAME}{path}').content


app.run( debug=True)