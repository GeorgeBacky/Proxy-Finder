# All links by search 
lnks=driver.find_elements_by_tag_name("a")
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute('href'))



# Click random links in site [ IN PROGRESS ]
while True:
    try:
        # find element using css selector
        links = browser.find_elements_by_css_selector('.post-img-wrap')
        print('Im workinggg')
        # create a list and chose a random link
        l = links[randint(0,len(links)-1)]

        # click link
        l.click()

        # check link
        new_page = browser.current_url

        # if link is the same, keep looping
        if new_page == current_page:
            continue
        else:
            # break loop if you are in a new url
            break
    except:
        continue



#  Sending keys

    timer
    browser.send_Keys(Keys.CONTROL + Keys.TAB)
    timer


# Testing code for switching tabsss :D DD
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
browser.get("https://accounts.google.com/signup")

browser.find_element_by_link_text("Help").click()

#prints parent window title
print("Parent window title: " + driver.title)

#get current window handle
p = browser.current_window_handle

#get first child window
chwd = browser.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
    browser.switch_to.window(w)
break
time.sleep(0.9)
print("Child window title: " + browser.title)
browser.quit()