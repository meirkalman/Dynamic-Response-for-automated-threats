import time
from flask import *


def abort_503():
    abort (503)


def sleep_abort():
    time.sleep(10)
    abort(503)


def empty_response():
    return "", 200


def fake_response():
    index = "FAKE_Juice_Shop.html"
    return render_template(index)

def hold_session(s):
    s.keep_alive = True
    s.status_code = 200
    return "", s.status_code