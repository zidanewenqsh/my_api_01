"""
Python3 JSON模块的使用
参考链接:https://docs.python.org/3/library/json.html
这里只是介绍最常用的dump、dumps和load、loads
"""

import json

# 自定义了一个简单的数据（Python中的字典类型），要想Python中的字典能够被序列化到json文件中请使用双引号！双引号！双引号！
data_obj = {
    "北京市": {
        "朝阳区": ["三里屯", "望京", "国贸"],
        "海淀区": ["五道口", "学院路", "后厂村"],
        "东城区": ["东直门", "崇文门", "王府井"],
    },
    "上海市": {
        "静安区": [],
        "黄浦区": [],
        "虹口区": [],
    }
}

# ---------------------------------------------------分割线------------------------------------------------------------


"""
dumps：序列化一个对象
sort_keys：根据key排序
indent：以4个空格缩进，输出阅读友好型
ensure_ascii: 可以序列化非ascii码（中文等）

"""
s_dumps = json.dumps(data_obj, sort_keys=True, indent=4, ensure_ascii=False)
print(s_dumps)

# ---------------------------------------------------分割线------------------------------------------------------------


"""
dump：将一个对象序列化存入文件
dump()的第一个参数是要序列化的对象，第二个参数是打开的文件句柄
注意打开文件时加上以UTF-8编码打开

* 运行此文件之后在统计目录下会有一个data.json文件，打开之后就可以看到json类型的文件应该是怎样定义的

"""
with open("data.json", "w", encoding="UTF-8") as f_dump:
    json.dump(data_obj, f_dump, ensure_ascii=False)
# print(s_dump) None

# ---------------------------------------------------分割线------------------------------------------------------------


"""
load：从一个打开的文件句柄加载数据
注意打开文件的编码

"""
with open("data.json", "r", encoding="UTF-8") as f_load:
    r_load = json.load(f_load)
print(r_load)

# ---------------------------------------------------分割线------------------------------------------------------------


"""
loads： 从一个对象加载数据

"""
r_loads = json.loads(s_dumps)
print(r_loads)

arg = '{"bakend": "www.oldboy.org", "record": {"server": "100.1.7.9", "weight": 20, "maxconn": 30}}'

# a = json.loads(input('请输入添加的数据：'),encoding='utf-8')
# print(a)
