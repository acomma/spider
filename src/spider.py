# -*- coding: utf-8 -*-

from collections import deque
from urllib.parse import urljoin
import re

from downloader import download

waiting_queue = deque()
downloaded_set = set()

seed_url = "http://example.webscraping.com/"
waiting_queue.append(seed_url)

def extract_url(page):
    if not page:
        return None
    # 提取URL正则表达式
    url_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return url_regex.findall(page)

def crawl():
    while(True):
        if not waiting_queue:
            break
    
        current_url = waiting_queue.popleft()
        page = download(current_url)

        links = extract_url(page.decode('utf-8'))
        for link in links:
            if link == "#":
                continue
            print(link)
            complete_link = urljoin(seed_url, link)
            if complete_link not in downloaded_set:
                waiting_queue.append(complete_link)
        downloaded_set.add(current_url)

if __name__ == "__main__":
    crawl()
