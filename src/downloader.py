# -*- coding: utf-8 -*-

import urllib.request

def download(url):
    if not url:
        return None
    # 返回的结果为byte类型
    page = urllib.request.urlopen(url).read()
    return page.decode('utf-8')