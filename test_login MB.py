# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver

mobileEmulation={'deviceName':'iPhone 6'}
options=webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument('--proxy-server=socks5://192.168.1.42:55551')      # 浏览器代理配置
driver=webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
driver.get('https://www.jjshouse.com/login.php?back=https://www.jjshouse.com/')
sleep(2)
#登录
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[1]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[1]/div[1]/input').send_keys('qwe1@tetx.com')
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[2]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[2]/div[1]/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[3]/button').click()
sleep(2)
print(driver.current_url)
URL = driver.current_url         # current_url 方法可以得到当前页面的URL
if URL=='https://www.jjshouse.com/':
    print('登录成功')
else:
    print('登录失败')