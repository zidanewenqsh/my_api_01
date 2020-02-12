import urllib
import re
from urllib import request

# def gethtml(url):
#     req = request.Request(url)
#     req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
#     response = request.urlopen(req)
#     html = response.readlines()
#     return html

# url = r"https://www.169tp.com/gaogensiwa/"
# req= request.Request(url)
# req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
# response = request.urlopen(req)
# # html = response.read().decode("utf-8")
# html = response.readlines()
# html = gethtml(url)

# print(html)
# pattern = r'(\A<a href(.*)https://www.169tp.com/gaogensiwa(.*)\.html)'
# pattern_1 = r'<a href(.*)https://www.169tp.com/gaogensiwa(.*)\.html'
# pattern_2 = r'www.169tp.com/gaogensiwa(.*)\.html'
# num = 0
# dataset = set()

def gethtml(url):
    req = request.Request(url)
    req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
    response = request.urlopen(req)
    html = response.readlines()
    return html
def getsearch(pattern, data):
    return re.search(pattern, str(data), re.M | re.S).group()
# for line in html:
#     # print(type(line))#<class 'bytes'>
#     # print(str(line))
#     # break
#     line_1 = re.search(pattern_1, str(line), re.M|re.S)
#
#     if line_1 != None:
#         # print(line_1)
#         line_1_ = re.search(pattern_2,str(line), re.M|re.S)
#         # print(line_2)
#         url_1 = "https://" + line_1_.group()
#         print(url_1)
#         html_1 = gethtml(url_1)
#         # dataset.add(url_1)
#         # req_1 = request.Request(url_1)
#         # req_1.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
#         # response_1 = request.urlopen(req_1)
#         # html_1
#         #
# print(num)
# print(len(dataset))
dataset = set()
for i in range(1,638):
    url = "https://www.169tp.com/gaogensiwa/list_3_{0}.html".format(i)
    html = gethtml(url)
    pattern = r'<a href(.*)https://www.169tp.com/gaogensiwa(.*)\.html'

    for line in html:
        # print(line)
        line_ = re.search(pattern, str(line),re.M|re.S)
        if line_ != None:
            start = line_.start()+9
            end = line_.end()
            # print(start,end)
            # print(line_)
            print(str(line)[start:end])
            dataset.add(str(line)[start:end])


    if i>0:
        break
print(len(dataset))

imgsrcset = set()
for i,url in enumerate(dataset):
    print(url)
    html = gethtml(url)
    # pattern = r'<a href=(.*?)\d.html">2</a>'
    pattern = r"img src(.*?).jpg"
    '<a href="44089_2.html">2</a>'
    for line in html:
        # print(line)
        line_ = re.search(pattern, str(line),re.M|re.S)
        if line_ != None:
            # print(line_)
            start = line_.start()+9
            end = line_.end()
            # print(start,end)
            # print(line_)
            # print(str(line)[start:end])
            img = str(line)[start:end]
            if img.startswith("http"):
                imgsrcset.add(img)

        pattern_1 = r'\d{1,5}_\d{1,2}.html'
        line_1 = re.findall(pattern_1, str(line), re.M | re.S)
        if line_1 != []:
            # print(line)
            print(set(line_1))
            newnet = url[0:-10]
            print(newnet)
            for item in set(line_1):
                newnet_ = newnet + item
                print(newnet_)


        # pattern_1 = r'\d{1,5}_\d{1,2}.html'
        # line_1 = re.search(pattern_1,str(line),re.M|re.S)
        # # print(type(line_1))
        # # print(line_1)
        # if line_1 != None:
        #     print(line_1)
    if i>10:
        break

for img in imgsrcset:
    print(img)