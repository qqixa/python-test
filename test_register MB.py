# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
import random

def get_userNameAndPassword():    #随机获取用户名和密码
    usableName_char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 可作为用户名的字符!@#$%^&*()_+=-><:}{?/
    usablePassword_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890"  # 可作为密码的字符，根据所需可适当增减
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

mobileEmulation={'deviceName':'iPhone 6'}
options=webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument('--proxy-server=socks5://192.168.1.42:55551')      # 浏览器代理配置
driver=webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
driver.get('https://www.jjshouse.com/login.php?back=https://www.jjshouse.com/')
sleep(2)
#注册
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div[2]').click()
sleep(2)

username, passwd = get_userNameAndPassword()
print(f"username is: {username} and password is: {passwd}")

driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[1]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[1]/div[1]/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[2]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[2]/div[1]/input').send_keys(passwd)
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[3]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[3]/div[1]/input').send_keys(passwd)
driver.find_element_by_xpath('//*[@id="register-panel"]/form/div[5]/button').click()
print('注册成功')
