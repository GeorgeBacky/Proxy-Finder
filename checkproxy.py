import random
import os , sys
import chromedriver_autoinstaller
from selenium import webdriver
proxy_list = []
f = open (os.path.join(sys.path[0],'proxies.txt'), 'r')
for line in f:
    line.replace('\n', "")
    proxy_list.append(line)
    # print(line)
f.close()
print("Finded proxies:",(len(proxy_list)))
PROXY = random.choice(proxy_list)
print('The proxy is:',PROXY)
chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s'%PROXY)
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://google.gr/')


driver.quit()