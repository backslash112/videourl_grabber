import time
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


auth_url = 'https://m.xinli001.com/account/login'
chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"

driver = webdriver.Chrome(chromedriver)
#urls = ['https://m.xinli001.com/lesson/playView?play_id={0}&id=67'.format(x) for x in range(470, 475)]
#
#time.sleep(10)
#for url in urls:
#    driver.execute_script('''window.open("{0}", "_blank");'''.format(url))
#    driver.get(url)
#    print('hi')
#    driver.find_element_by_id('')
#
driver.get(auth_url)
#driver.find_element_by_class_name('tabs')[0].click()
driver.find_elements_by_xpath("//*[contains(text(), '账号密码登录')]")[0].click()
time.sleep(0.5)
driver.find_element_by_id('login_username').send_keys('<username>')
driver.find_element_by_id('login_password').send_keys('<pwd>')
#driver.find_elements_by_xpath("//*[contains(text(), '登录')]")[0].click()
driver.find_element_by_xpath("//a[@type='submit']").click()
time.sleep(1)

driver.get('https://m.xinli001.com/lesson/playView?play_id=442&id=67')

def save(tup):
    save_file("/Users/cunyang/Downloads/video.txt", tup)
    
def save_file(file_name, tup):
    with open(file_name, 'a+') as f:
            # separate each field with tab for Anki
            f.write("{0}; {1}\n".format(tup[0], tup[1]))

def get_video():
    
    title = ""
    url = ""
    if driver.find_element_by_xpath("//div[@class='video-small-title']"):
        title = driver.find_element_by_xpath("//div[@class='video-small-title']").text
        
    print(title)
    time.sleep(0.5)
    video_html = driver.find_element_by_id('video-player-container').get_attribute('innerHTML')
#    print(str(video_html))
    if re.findall('https://.+mp\w', str(video_html)):
        url = re.findall('https://.+mp\w', str(video_html))[0]
        print(url)
    
    if title and url:
        save((title, url))
        
    time.sleep(0.5)
    if driver.find_elements_by_xpath("//div[@class='class-link-title']"):
        driver.find_elements_by_xpath("//div[@class='class-link-title']")[-1].click()
        time.sleep(0.5)
        get_video()

get_video()