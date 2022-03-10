
import time
from fake_responses import *
import requests
from flask import *
from requests import *


app = Flask('__main__')
SITE_NAME = 'https://www.ynet.co.il/home/0,7340,L-8,00.html'


def detect_attack():
    return True


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    if detect_attack():
        # option 1:
        # abort_503()
        # option 2
        # return empty_response()
        # option 3:
        # sleep_abort()
        # option 4:
        index = "OWASP_Juice_Shop.html"
        return fake_response()

    return get(f'{SITE_NAME}{path}').content


app.run( debug=True)