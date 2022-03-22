import requests

DOS_ATTACK_ATTEMPTS = 10


for i in range(DOS_ATTACK_ATTEMPTS):
    session = requests.Session()
    res = session.get('http://localhost:5000/')
    print(res.text)