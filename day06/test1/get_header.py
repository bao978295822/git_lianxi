import requests

# 准备数据
url = 'https://www.wanandroid.com/user/login'
shuju = {"username": "bao", "password": "123456"}
r = requests.post(url=url, data=shuju)
cookie1 = r.cookies
print(cookie1)
header1 = {}
# header1["Cookie"] = "JSESSIONID=EFCEF093638A0B30585BC88C79CC38D5" #cookie有时效性，过段时间就过期了
header1["Cookie"] = 'JSESSIONID=A20C74E4D6F46C75B8848450B2394C92'

# 个人信息接口
url = "https://wanandroid.com//user/lg/userinfo/json"
re2 = requests.get(url=url, headers=header1)
print(re2.text)
