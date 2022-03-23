import requests

"""
#post data for hack-yourself-first.com
@app.route('/Account/Login',methods=['POST', 'GET'])
def login():
    sender_ip = request.remote_addr
    raw_data = request.get_data(as_text=True)
    payload_array = raw_data.split("&")
    email = (payload_array[0].split("="))[1].replace("%40","@")
    password = (payload_array[1].split("="))[1]
    # input validation
    if (payload_array[0].split("="))[0] != "Email" or (payload_array[1].split("="))[0] != "Password":
        return 'Invalid Parameters in Your Json'

    if detect_brute_force_password(email, password, sender_ip):    # extract ip and time
        return abort_503()
    payload = {'Email': email, 'Password': password}
    return post(f'{SITE_NAME}/Account/Login',data=payload).content

"""


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
