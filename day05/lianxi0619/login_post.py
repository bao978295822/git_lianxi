import requests

shuju={"username":"bao","password":"123456"}
url="https://wanandroid.com/user/login"
r=requests.post(url,shuju)
print(r.status_code)
print(r.headers)
# print(r.request)
