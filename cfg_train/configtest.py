import configparser
# 加载现有配置文件
conf = configparser.ConfigParser()
# 写入配置文件
# conf.add_section('config') #添加section
# 添加值
# conf.set('config', 'v1', '100')
# conf.set('config', 'v2', 'abc')
# conf.set('config', 'v3', 'true')
# conf.set('config', 'v4', '123.45')
# 写入文件
# with open('conf.ini', 'w') as fw:
#     conf.write(fw)
v1 = 10
# 读取配置信息
conf.read("cfg.ini")
secs = conf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
print(secs)

options = conf.options("net_01_1")  # 获取某个section名为Mysql-Database所对应的键
print(options)

items = conf.items("net_01_1")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)

host = conf.get("net_01_1", "EPOCH")  # 获取[Mysql-Database]中host对应的值
print(host)
v1_ = conf.getint('net_01_1', 'BATCHSIZE')
# v2 = conf.get('config', 'v2')
# v3 = conf.getboolean('config', 'v3')
# v4 = conf.getfloat('config', 'v4')
# print('v1:', v1)
# print('v2:', v2)
# print('v3:', v3)
# print('v4:', v4)
# conf.read_string()
v5_=conf.get('net_01_1', 'NUMWORKERS')
print(v5_,type(v5_))