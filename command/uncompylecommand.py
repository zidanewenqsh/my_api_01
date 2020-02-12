import os
import sys


def displayFile(file):
    unPath = sys.executable#D:\MySoft\Anaconda3
    unPath = unPath[0: unPath.rfind(os.sep)]

    '''
    find是从字符串左边开始查询,查询到的第一个子字符串的下标(下标从0开始)
    rfind是从字符串右边开始查询,查询到的第一个子字符串的下标(下标从0开始)'''
    # newname = file[0:file.rfind('.')] + '.py'
    # newname = ''.join([file.split(os.sep)[-1].split('.')[0],".py"])
    newname = os.path.join(os.path.dirname(file), "".join([os.path.basename(file).split('.')[0],'.py']))
    # command = r"python -u " + unPath + r"\scripts\uncompyle6.exe " + file + ">" + newname
    command = r"uncompyle6 " + file + ">" +newname#比上面的写法好
    print(unPath.rfind(os.sep))
    print(unPath)
    print(newname)
    print(command)

    try:
        os.system(command)
    except Exception as e:
        print(file)


if __name__ == '__main__':
    print(os.sep)
    print(sys.executable)
    # print unPath
    print('init')
    displayFile(r"D:\test\__pycache__\uncompiletest01.cpython-37.pyc")
    print('finished')