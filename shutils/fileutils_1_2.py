import os
import time
import shutil


# from tool import utils

def makedir(path):
    '''
    如果文件夹不存在，就创建
    :param path:路径
    :return:路径名
    '''
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def countFiles(path, *path_1):
    '''
    单个或多个路径中包含的文件和文件夹计数
    :param path:
    :param path_more:
    :return:
    '''

    # 定义变量
    dirs_num = 0
    files_num = 0
    '''
    RecursionError: maximum recursion depth exceeded while calling a Python object
    发现python默认的递归深度是很有限的（默认是1000），因此当递归深度超过999的样子，就会引发这样的一个异常。
    '''
    if len(path_1) != 0:
        for path_ in path_1:
            print("aaaa", path_)
            files_num_, dirs_num_ = countFiles(path_)
            print("aaa", files_num_, dirs_num_)
            files_num += files_num_
            dirs_num += dirs_num_
    # 判断文件夹存在
    if os.path.exists(path) and os.path.isdir(path):  # 用walk必做判断是否是文件夹，是文件则不运行，文件不存在也不运行，但不报错
        for root, dirs, files in os.walk(path):
            dirs_num += len(dirs)
            files_num += len(files)
        return files_num, dirs_num
    return 0, 0


def filefunctiontime(function, src_dir):
    start_time = time.time()  # 开始时间
    print("The number of file in this dir is ", countFiles(src_dir)[0])
    # function
    print("The count of files already treated is: ", function)
    end_time = time.time()
    time_used = end_time - start_time
    print("The time of treating used is: ", "%.2fh" % (time_used / 3600) if time_used >= 3600 else "%.2fmin" % (
            time_used / 60) if time_used >= 60 else "%.2fs" % time_used)


def copydirs(src_dir, dst_dir, cover=False, timethreshold=1, outputthreshold=1000):
    count = 0  # 总复制文件计数
    count_eachtime = 0  # 单位时间复制文件计数
    start_time = time.time()  # 开始时间
    time_temp = start_time  # 临时时间，用于计算单位时间
    # 判断文件夹存在

    if os.path.isfile(src_dir):
        return

    makedir(dst_dir)
    for file in os.listdir(src_dir):

        file_src = os.path.join(src_dir, file)
        file_dst = os.path.join(dst_dir, file)
        if os.path.isfile(file_src):

            print("file_src1", file_src)
            print("file_dst1", file_dst)
            if cover:
                shutil.copy(file_src, file_dst)
                count += 1
                count_eachtime += 1
            elif not os.path.exists(file_dst):
                shutil.copy(file_src, file_dst)
                count += 1
                count_eachtime += 1
            check_time = time.time()
            time_inter = check_time - time_temp

            if count % outputthreshold == 0 and count > 0:
                print("the number of files is copied successfully:", count)

            if time_inter > timethreshold:
                print("number of copy in {0}s: {1}, time already used: {2}s".format(timethreshold, count_eachtime,
                                                                                    int(check_time - start_time)))
                time_temp = check_time
                count_eachtime = 0

        elif os.path.isdir(file_src):
            print("file_src2", file_src)
            print("file_dst2", file_dst)
            copydirs(file_src, file_dst, cover)
    return count


def copyfiles(src_path, dst_path, cover=False, timethreshold=1, outputthreshold=1000):
    '''
    文件夹复制
    :param path:
    :param timethreshold: 计算单位时间复制量的计算间隔
    :param outputthreshold: 每隔一段时间查看总复制结果的时间间隔
    :return:
    '''
    # 定义变量
    count = 0  # 总复制文件计数
    count_eachtime = 0  # 单位时间复制文件计数
    start_time = time.time()  # 开始时间
    time_temp = start_time  # 临时时间，用于计算单位时间
    # 判断文件夹存在
    if os.path.exists(src_path) and os.path.isdir(src_path):
        # 计算要复制的文件总数
        # print("The number of file in this dir is ", countFiles(src_path)[0])
        # 复制文件
        for root, dirs, files in os.walk(src_path):
            for i, file in enumerate(files):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_path, file)
                if cover:
                    shutil.copy(src_file, dst_file)
                    count += 1
                    count_eachtime += 1
                elif not os.path.exists(dst_file):
                    shutil.copy(src_file, dst_file)
                    count += 1
                    count_eachtime += 1
                check_time = time.time()

                # 中间输出
                if i % outputthreshold == 0 and i > 0:  # i==0时不计数
                    print("the number of files is copied successfully:", count)

                time_inter = check_time - time_temp

                if time_inter > timethreshold:
                    print("number of copy in {0}s: {1}, time already used: {2}s".format(timethreshold, count_eachtime,
                                                                                        int(check_time - start_time)))
                    time_temp = check_time
                    count_eachtime = 0

    return count


def movefiles(src_dir, dst_dir, cover=False, timethreshold=1, outputthreshold=1000):
    '''
    文件夹移动
    :param path:
    :param timethreshold: 计算单位时间移动量的计算间隔
    :param outputthreshold: 每隔一段时间查看总移动结果的时间间隔
    :return:
    '''
    # 定义变量
    count = 0  # 总移动文件计数
    count_eachtime = 0  # 单位时间移动文件计数
    start_time = time.time()  # 开始时间
    time_temp = start_time  # 临时时间，用于计算单位时间
    # 判断文件夹存在

    # if os.path.isfile(src_path):
    #     roots = os.path.dirname(self.src_path)
    #     file_name = os.path.basename(self.src_path)
    #     self.send_file(roots, file_name, src_path, self.ip_port, self.bufsize)
    # elif os.path.isdir(src_path):
    #     for roots, dirs, files in os.walk(src_path):
    #         # file_path = os.path.join(roots, files)
    #         for file_name in files:
    #             self.send_file(roots, file_name, src_path, self.ip_port, self.bufsize)

    if os.path.exists(src_dir) and os.path.isdir(src_dir):
        # 计算要移动的文件总数
        print("The number of file in this dir is ", countFiles(src_dir)[0])
        src_dir = os.path.abspath(src_dir)

        # 移动文件
        for roots, dirs, files in os.walk(src_dir):
            for i, file in enumerate(files):
                src_file = os.path.join(roots, file)

                # if not os.listdir()
                # dst_file = os.path.join(dst_path,file)
                # file_path = os.path.join(roots, files)
                # dir_rel = '\\'.join(os.path.dirname(file_path).split('\\')[1:])
                dir_relativ = os.path.dirname(src_file)[len(src_dir) + 1:]  # 获取相对文件夹路径
                # print(dir_relativ)
                # print(type(dir_relativ))
                dst_dir_ = os.path.join(dst_dir, dir_relativ)
                makedir(dst_dir_)
                dst_file = os.path.join(dst_dir_, file)
                # print(dst_file)

                if cover:
                    shutil.move(src_file, dst_file)
                    count += 1
                    count_eachtime += 1
                elif not os.path.exists(dst_file):
                    shutil.move(src_file,dst_file)
                    count += 1
                    count_eachtime += 1
                check_time = time.time()

                # 中间输出
                if i % outputthreshold == 0 and i > 0:  # i==0时不计数
                    print("the number of files is moved successfully:", count)
                    pass
                time_inter = check_time - time_temp

                if time_inter > timethreshold:
                    print("number of move in {0}s: {1}, time already used: {2}s".format(timethreshold, count_eachtime,
                                                                                        int(check_time - start_time)))
                    time_temp = check_time
                    count_eachtime = 0
            # for dir in dirs:
            #     src_dir_ = os.path.join(roots, dir)
            #     print("src", src_dir_)
            #     if not os.listdir(src_dir_):  # 判断文件夹为空
            #         print("empty", src_dir_)
            #         # os.removedirs(src_dir_) # 删除空文件夹

    return count


def deletefiles(path, timethreshold=1, outputthreshold=1000):
    '''
    删除文件夹中的所有文件并计时
    :param path:
    :param timethreshold: 计算单位时间删除量的计算间隔
    :param outputthreshold: 每隔一段时间查看总删除结果的时间间隔
    :return:
    '''
    # 定义变量
    count = 0  # 总删除文件计数
    count_eachtime = 0  # 单位时间删除文件计数
    start_time = time.time()  # 开始时间
    # filenum_todel = 0  # 要删除的文件总数变量,因为用了countFiles函数，所以没用了
    time_temp = start_time  # 临时时间，用于计算单位时间
    # 判断文件夹存在
    if os.path.exists(path) and os.path.isdir(path):
        # 计算要删除的文件总数
        # for root, dirs, files in os.walk(path):
        #     filenum_todel += len(files)
        print("The number of file in this dir is ", countFiles(path)[0])
        # 删除文件
        for root, dirs, files in os.walk(path):
            for i, file in enumerate(files):
                file_todel = os.path.join(root, file)
                os.remove(file_todel)
                check_time = time.time()

                # 中间输出
                if i % outputthreshold == 0 and i > 0:  # i==0时不计数
                    print("the number of files is deleted successfully:", count)

                count += 1
                count_eachtime += 1
                time_inter = check_time - time_temp

                if time_inter > timethreshold:
                    print("number of delete in {0}s: {1}, time already used: {2}s".format(timethreshold, count_eachtime,
                                                                                          int(check_time - start_time)))
                    time_temp = check_time
                    count_eachtime = 0

    return count


if __name__ == '__main__':
    print(1)
    srcpath = r"D:\a\src"
    dstpath = r"D:\a\dst"
    movefiles(srcpath, dstpath, cover=True)
    s1 = r"D:\a\src\aaa\c"
    # os.remove(s1)
    # os.removedirs(s1)
