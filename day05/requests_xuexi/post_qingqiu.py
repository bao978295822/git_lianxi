import requests

#准备数据
url = 'https://wanandroid.com/user/login'
shuju={"username":"bao","password":"123456"}
r=requests.post(url=url,data=shuju)
print(r.status_code)
print("text",r.text)
print(r.json())
print(type(r.json()))

print(r.headers)
print(r.headers["date"])
print("字符编码",r.encoding)
print("url",r.url)
print("查看耗时",r.elapsed)