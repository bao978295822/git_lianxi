import json
data='{"data":{"admin":false,"chapterTops":[],"coinCount":10,"collectIds":[],"email":"","icon":"","id":134205,"nickname":"bao","password":"","publicName":"bao","token":"","type":0,"username":"bao"},"errorCode":0,"errorMsg":""}'

#将json转化为字典
print(data)
print(type(data))
print(json.loads(data))
print(type(json.loads(data)))

#将字典转为json

dict1={"name":"xiaomign","age":20}
data3=json.dumps(dict1)
print(data3)
print(type(data3))