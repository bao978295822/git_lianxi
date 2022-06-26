import requests

# 准备数据
url = 'https://www.wanandroid.com/user/login'
shuju = {"username": "bao", "password": "123456"}
s = requests.session()
print(s)
print(s.cookies)
r = s.post(url=url, data=shuju)
print(r.text)
cookie1 = r.cookies
print(cookie1)

# 个人信息接口
url = "https://wanandroid.com//user/lg/userinfo/json"
re2 = s.get(url=url)
print(re2.text)
print("测试推送")
