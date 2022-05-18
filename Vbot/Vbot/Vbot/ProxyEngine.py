# Youtube View Bot
# Developed By: ef1500
# For eren

import urllib.request
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import colorama
import time
from colorama import Fore, Back, Style

def GetViews(url, proxy):
    print('Hitting the url with proxy: ' + Fore.GREEN + str(proxy))
    # This is the function that will get us the views.
    # To accomadate multithreading, this function only takes in ONE proxy instead of loading an entire file.
    #pxy = 'http://' + proxy
    #proxies={'http': pxy}
    #px_sp = urllib.request.ProxyHandler(proxies)
    #opener = urllib.request.build_opener(px_sp)
    #urllib.request.install_opener(opener)
    #response = urllib.request.urlopen(url)
    #time.sleep(5)
    #if str(response.getcode()) == '200':
    #    print(Fore.GREEN + 'Successfully Hit url with proxy: ' + Fore.RED + str(proxy))
    #else:
    #    print(Fore.RED + 'FAILED TO HIT URL WITH PROXY: ' + str(proxy))
    ua = UserAgent()
    userAgent = ua.random
    print("USER AGENT: " + str(userAgent))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % str(proxy))
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome = webdriver.Chrome(options=chrome_options)
    try:
        chrome.get(str(url))
    except:
        pass
    delay = 20
    try:
        element = WebDriverWait(chrome, delay).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.html5-video-player')))
        print(Fore.GREEN + 'Successfully Hit url with proxy: ' + Fore.RED + str(proxy))
    except:
        print(Fore.RED + 'FAILED TO HIT URL WITH PROXY: ' + str(proxy))
        chrome.close()

def loadProxies(source):
    # This will take the proxies from the proxy file and then put them into a list for later usage
    proxies = []
    with open(source, 'r', encoding='utf8') as yuzu:
        for line in yuzu:
            proxies.append(str(line))
    return proxies