import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("window-size=1400,600")
from fake_useragent import UserAgent
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
chromedriver_autoinstaller.install()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://whoer.net/')
driver.sendKeys(Keys.F5);
time.sleep(5)
driver.sendKeys(Keys.F5);
time.sleep(100)
driver.quit()