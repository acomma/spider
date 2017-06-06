# -*- coding: utf-8 -*-

from collections import deque
import urllib.request

waiting_queue = deque()
downloaded_set = set()

seed_url = "http://example.webscraping.com/"
waiting_queue.append(seed_url)

def download(url):
    return urllib.request.urlopen(url).read();

def extract_url(page):
    pass

if __name__ == "__main__":
    while(True):
        if not waiting_queue:
            break
	
        current_url = waiting_queue.popleft()
        page = download(current_url)
        downloaded_set.add(current_url)

    for url in downloaded_set:
        print(url)
