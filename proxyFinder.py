import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def browse_proxy_list():
    # selenium chrome browser
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options = chrome_options)
    
    # browse spys.one proxy site
    browser.get("https://spys.one/free-proxy-list/TR/")
    browser.execute_script("document.getElementById('xpp').selectedIndex = 5; document.getElementById('xpp').onchange();")
    
    # retrieve HTML elements and remove first element (table header)
    proxy_list = browser.find_elements_by_xpath("//tr[@class='spy1xx']")
    proxy_list1 = browser.find_elements_by_xpath("//tr[@class='spy1x']")
    proxy_list.pop(0)
    proxy_list1.pop(0)
    
    proxiesList = []
    print('Adding to text file proxies!')
    for i in range(len(proxy_list)):
        proxy_server = browser.find_element_by_xpath("//tr[@class='spy1x'][" + str(i+2) + "]//td[1]//font[@class='spy14']").text
        proxy_server1 = browser.find_element_by_xpath("//tr[@class='spy1xx'][" + str(i+2) + "]//td[1]//font[@class='spy14']").text
        # print(proxy_server,'\n',proxy_server1)
        proxiesList.append(proxy_server)
        proxiesList.append(proxy_server1)
        with open('proxies.txt', 'w') as f:
            for proxies in proxiesList:
                f.write("{}\n".format(proxies))
    print('Success')
# browse_proxy_list()



def browse_proxy_list_2():
    # selenium chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe',chrome_options = chrome_options)
    
    # browse free-proxy.cz proxy site
    browser.get("http://free-proxy.cz/en/proxylist/country/TR/http/ping/all")
    
    # click export 
    proxy_list = browser.find_element_by_xpath("//span[@id='clickexport']").click()
    proxy_server = browser.find_element_by_xpath("//div[@id='zkzk']").get_attribute("innerHTML")
    proxiesList = []
    for i in range(0,1):
        proxy_server = browser.find_element_by_xpath("//div[@id='zkzk']").get_attribute("innerHTML")
        print(proxy_server,'\n')
        print('Adding to text file proxies!')
        proxiesList.append(proxy_server)
        with open('proxies.txt', 'w') as f:
            for proxies in proxiesList:
                f.write("{}\n".format(proxies))
        infile = 'proxies.txt'
        outfile = 'proxiesList2.txt'
        delete_list = ["<br>", "<br>", "<br>"]
        with open(infile) as fin, open(outfile, "w+") as fout:
            for line in fin:
                for word in delete_list:
                    line = line.replace(word, "\n")
                fout.write(line)
    print('Success')
    time.sleep(10)
    browser.close();
browse_proxy_list_2()

# browse_proxy_list()