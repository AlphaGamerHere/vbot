# Youtube View Bot
# Developed By: ef1500
# For eren

# Multiengine.py - This is the file that is responsible for multithreading and multiprocessing across cores. This might take up some CPU usage,
# Don't think that it will be that much of an issue.

from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from functools import partial
import ProxyEngine as yuu
import multiprocessing as yuzu
import threading as mei

def RunThreads(proxy, url):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 400) as executor:
        p_viewer = {executor.submit(yuu.GetViews, proxies, url): proxies for proxies in proxy}
        try:
            data = future.result()
        except Exception as exc:
            print('generated an exception')