import requests

# 准备数据
url = 'https://www.wanandroid.com/user/login'
shuju = {"username": "bao", "password": "123456"}
r = requests.post(url=url, data=shuju)
print(r.headers)
print(r.text)

cookie1 = r.cookies
print(cookie1)

# 个人信息接口
url = "https://wanandroid.com//user/lg/userinfo/json"
re2 = requests.get(url=url,cookies=cookie1)

print(re2.text)
