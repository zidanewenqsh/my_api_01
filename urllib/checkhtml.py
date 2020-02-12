import re
from urllib import request
def gethtml(url):
    req = request.Request(url)
    req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
    response = request.urlopen(req)
    html = response.readlines()
    return html
def getsearch(pattern, data):
    return re.search(pattern, str(data), re.M | re.S).group()
opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]

url = r"https://www.169tp.com/gaogensiwa/2017/0809/39392.html"

opener.open(url)
html = gethtml(url)
for line in html:
    # print(line)
    pattern_1 = r'\d{1,5}_\d{1,2}.html'
    line_1 = re.findall(pattern_1, str(line), re.M | re.S)
    if line_1 != []:
        print(line)
        print(set(line_1))