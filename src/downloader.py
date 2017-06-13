# -*- coding: utf-8 -*-

import urllib.request

def download(url):
    if not url:
        return None
    try:
        # 返回的结果为byte类型
        page = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        return None

    return page.decode('utf-8')