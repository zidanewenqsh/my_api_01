import re
string = r'<a href="https://www.169tp.com/gaogensiwa/2017/0811/39409.html"'
pattern = r'<a href(.*)www.169tp.com/gaogensiwa(.*)\.html'
string = r"<a href=\'39418_2.html\'>"
string = r'<a href="#"'
string = r'<a href="https://www.169tp.com/gaogensiwa/2016/0326/35647.html" '
string =r'a href="39418_3.html"'
pattern = r"\d{1,5}_\d{1,2}.html"
# pattern = r"\d{1,5}"
# string1 = re.search(pattern,string)
string1 = re.search(pattern,string, re.M|re.S)
print(type(string1))
print(str(string1))
print(str(string1).find("html"))
# print(help(re.Match))
print(string1.group())
print(string1.groupdict())
print(string1.start())
if not None:
    print("\'")