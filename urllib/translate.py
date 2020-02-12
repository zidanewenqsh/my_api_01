from urllib import request,parse
import json
# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule" #{"errorCode":50} 其中的_o去掉错误则解决
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}

with open("data.txt",encoding='utf-8') as f:
    for line in f.readlines():
        datas = line.split(":")
        data[datas[0]] = datas[1].strip()
print(data)
print(type(data))
data = parse.urlencode(data).encode("utf-8")
# response = request.urlopen(url,data)
req = request.Request(url,data)

print(req.headers)#{}
req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
print(req.headers)
response = request.urlopen(req)
html = response.read().decode("utf-8")
print(html)
print(type(html))
# target = json.load(html)#AttributeError: 'str' object has no attribute 'read'
target = json.loads(html)#load是加载，loads为解码
print(target)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt'] ) )