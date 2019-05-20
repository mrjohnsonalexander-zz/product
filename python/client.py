import requests

myData = {'key1': 'value1'}

r = requests.post(url = "http://localhost:8081", data = myData)

respon = r.text
print("response == %s"%respon)
