import configparser
config = configparser.ConfigParser()

config.read(r"D:\PycharmProjects\mtcnn_02\src\cfg.ini")

EPOCH = 10000
BATCHSIZE = 256
NUMWORKERS = 4
SAVE_DIR = r"../save/20190910"
NETFILE_NAME = "net_01_1"
NETFILE_EXTENTION = "pt"
SAVEDIR_EPOCH = r"..\save\netbackup"
PIC_DIR = r"D:\datasets\save_10261_20190725\pic"
LABEL_DIR = r"D:\datasets\save_10261_20190725\label"
Test_IMG = r"../test/005290.jpg"
PRETRAINED_PNET = r"../param/pnet_07.pth"
PRETRAINED_RNET = r"../param/rnet_07_4.pth"
PRETRAINED_ONET = r"../param/onet_07_4.pth"
LOGDIR = r"../log/20190910"
RECORDPOINT = 10
TESTPOINT = 100
ALPHA = 0.9
ISCUDA = True
CONTINUETRAIN = False
PRETRAINED = False
NEEDSAVE = False

items = config.items("net_01_1")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)
print(locals().keys())
for k,v in items:
    # print(k)
    if k.upper() in locals().keys():
        # print(k)
        locals()[k.upper()] = v
print(ALPHA)