from urllib import request, parse
import random
url = "https://www.whatismyip.com"
# url = "https://www.whatismyip.com.tw"
# url = "https://cn-proxy.com/"
# url = "http://715.169pp.net/169mm/201909/065/1.jpg"
iplist = ['124.156.108.71:82','101.231.104.82:80','39.106.205.147:80']
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
url = request.Request(url,headers=headers)
proxy_support = request.ProxyHandler({'http':random.choice(iplist)})
opener = request.build_opener(proxy_support)

request.install_opener(opener)
response = request.urlopen(url)
html = response.read().decode('gbk')
print(html)