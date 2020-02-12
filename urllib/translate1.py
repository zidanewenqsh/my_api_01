# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json

content = input("请输入：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
data['i']= content
data['type']='AUTO'

data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1524549963983'
data['sign']='fd4866c83ab536113ae1e62cfb486727'
data['doctype']= 'json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_REALTIME'
data['typoResult']='false'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

print(html)
print(type(html))
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt'] ) )