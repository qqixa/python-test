# -*- coding: utf-8 -*-
# _author_ = "qqx"
# date : 4/7/2020

from selenium import webdriver
from time import sleep
import random

def webdriver1():
    option = webdriver.ChromeOptions()
    option.add_argument('--proxy-server=socks5://192.168.1.42:55551')  # 浏览器代理配置
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()  # 窗口最大化
    timeout = 10
    driver.implicitly_wait(timeout)
    driver.get('https://www.jjshouse.com/')
    return driver

def get_userNameAndPassword():    #随机获取用户名和密码
    usableName_char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 用户名的字符!@#$%^&*()_+=-><:}{?/
    usablePassword_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890"  # 密码
    e_userName = []  # 定义一个临时List变量,使用list.append添加字符
    e_userPassword = []
    for i in range(8):
        e_userName.append(random.choice(usableName_char))
    for j in range(6):
        e_userPassword.append(random.choice(usablePassword_char))
    e_userName.append("@tetx.com")
    userName = ''.join(e_userName)
    userPassword = ''.join(e_userPassword)
    return userName, userPassword

def register(driver,username,userpassword):
    driver.find_element_by_id('login_register_li').click()  # 点击登录/注册按钮
    sleep(2)
    driver.find_element_by_id('continue-btn').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="email"]').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(userpassword)
    driver.find_element_by_xpath('//*[@id="password_again"]').send_keys(userpassword)
    driver.find_element_by_class_name('sign-up-btn').click()
    print('注册成功')


if __name__ == '__main__':
    handle = webdriver1()
    name, password = get_userNameAndPassword()
    print(f"用户名: {name} 密码: {password}")
    register(driver=handle,username=name,userpassword=password)