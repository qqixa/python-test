# -*- coding: utf-8 -*-
# _author_ = "qqx"
# date : 4/7/2020

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

def hover(self, by,value):                #添加鼠标悬浮定位功能
    element = self.findElement(by, value)
    ActionChains(self.driver).move_to_element(element).perform()

def webdriver1():
    option = webdriver.ChromeOptions()
    option.add_argument('--proxy-server=socks5://192.168.1.42:55551')  # 浏览器代理配置
    #option.add_argument('--proxy-server=socks5://192.168.9.102:10808')
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()  # 窗口最大化
    # timeout = 10
    # driver.implicitly_wait(timeout)
    return driver

def login(driver, account, passwd):
    driver.get('https://www.jjshouse.com/')
    sleep(2)
    driver.find_element_by_id('login_register_li').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="_email"]').click()
    driver.find_element_by_xpath('//*[@id="_email"]').send_keys(account)
    driver.find_element_by_id('_password').send_keys(passwd)
    driver.find_element_by_class_name('sign-btn').click()
    sleep(3)
    print(driver.current_url)
    URL = driver.current_url  # current_url 方法可以得到当前页面的URL
    if URL == 'https://www.jjshouse.com/':
        print('登录成功')
    else:
        print('登录失败')
    driver.find_element_by_xpath('//*[@id="signOrLogin"]/div/h6/em').click()    #sign out
    driver.find_element_by_xpath('//*[@id="signOrLogin"]/div/div/a[6]').click()
    print('退出登录')

if __name__ == '__main__':
    handle = webdriver1()
    login(driver=handle, account='qwe1@tetx.com',passwd='123456')      #正确的用户名和密码
