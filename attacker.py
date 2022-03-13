import requests



headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'Email':'dsfs@gmail.com','Password':'12345678'}

session = requests.Session()
session.keep_alive = False
res = session.post('http://127.0.0.1:5000/Account/Login',data=payload,headers = headers)


#print(res.content)
print(res.text)
