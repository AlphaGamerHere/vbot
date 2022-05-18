# Youtube View Bot
# Developed By: ef1500
# For eren

# engine.py - this is the file where it all comes together... the final file. If this works... wowzies.

import ProxyEngine as kotone
import MultiEngine as peko
import colorama
import threading
from colorama import Fore, Back, Style
import cacheEngine as pekora
import subprocess

colorama.init()

def main():
    print('Starting ef1500\'s viewbot...')
    subprocess.call('python cacheEngine.py', shell=True)
    Proxies = kotone.loadProxies('Proxies.txt')
    print('Loaded ' + Fore.GREEN + str(len(Proxies)) +Fore.WHITE+' Proxies!')
    url = input('Please Enter a Youtube url: ')
    print(Fore.GREEN + 'Hitting the url with ' + Fore.RED + str(len(Proxies)) + Fore.WHITE + " Proxies...")
    #peko.RunThreads(Proxies, url)
    for proxy in Proxies:
        thread = threading.Thread(target=kotone.GetViews, args=(url, str(proxy)))
        thread.start()
        thread.join()

if __name__ == "__main__":
    main()