import requests



headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'Email':'hiwedo2878@superyp.com','Password':'123456'}

session = requests.Session()
#session.keep_alive = False
res = session.post('http://127.0.0.1:5000/Account/Login',data=payload,headers = headers)


#print(res.content)
print(res.text)
