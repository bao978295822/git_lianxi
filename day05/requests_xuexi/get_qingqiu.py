import requests
# r=requests.get("http://www.baidu.com")
# print(r.status_code)

#准备数据
url='https://www.kuaidi100.com/query'
shuju={"type":"shunfeng","postid":"SF1409812533366"}
r=requests.get(url=url,params=shuju)
print(r.status_code)
print(r.text)
print(r.json())
print(type(r.json()))

print(r.headers)
print(r.headers["date"])
print("字符编码",r.encoding)
print("url",r.url)
print("查看耗时",r.elapsed)