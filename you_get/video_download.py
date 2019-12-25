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

    url = 'https://www.bilibili.com/video/av77881777?from=search&seid=13958931206012048776'

    # 视频输出的位置

    path = 'D:/test'

    download(url, path)
