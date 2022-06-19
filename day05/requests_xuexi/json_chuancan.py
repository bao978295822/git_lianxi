import requests

#准备数据
url = 'http://httpbin.org/post'
shuju={"username":"bao","password":"123456"}
#通过json方式来进行传参
r=requests.post(url=url,json=shuju)
print(r.status_code)
print("text",r.text)
print(r.json())
print(type(r.json()))
