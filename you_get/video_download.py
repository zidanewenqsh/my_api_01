# ！/usr/bin/env python

# -*-coding:utf-8-*-

import sys

import you_get


def download(url, path):
    # sys.argv = ['you-get', '-o', path, url]
    sys.argv = ['you-get', '--playlist', '-o', path, url] # (use --playlist to download all videos.)

    you_get.main()



if __name__ == '__main__':
    # 视频网站的地址

    url = 'https://www.bilibili.com/video/av82643703?from=search&seid=12161001519466991232'

    # 视频输出的位置

    path = 'D:\PycharmProjects\my_api_01\saves'

    download(url, path)
