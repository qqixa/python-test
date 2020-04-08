# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

mobileEmulation={'deviceName':'iPhone 6'}
options=webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument('--proxy-server=socks5://192.168.1.42:55551')      # 浏览器代理配置
driver=webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)

driver.get('https://www.jjshouse.com/login.php?back=https://www.jjshouse.com/')           #登录
sleep(2)
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[1]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[1]/div[1]/input').send_keys('qwe1@tetx.com')
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[2]/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[2]/div[1]/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login-panel"]/form/div[3]/button').click()
print ('登录成功')
print('账号qwe1@tetx.com 密码123456')
sleep(2)

driver.get('https://www.jjshouse.com/cart.php#/')
sum = driver.find_element_by_class_name('main-cart-title').text
print(sum)
while sum != 'Shopping Cart (0 Item)':                              #清空购物车
    driver.find_element_by_class_name('cart-item-remove').click()    #处理google的confirm弹框
    sleep(1)
    dig_confirm = driver.switch_to.alert
    sleep(1)
    dig_confirm.accept()  #点击“确认”按钮
   # dig_confirm.dismiss()  #点击“取消”按钮
    sleep(1)
    sum = driver.find_element_by_class_name('main-cart-title').text
    print(sum)

driver.get('https://www.jjshouse.com/-g4044')
print('g4044')
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[3]/button').click()
print('加购成功')
sleep(2)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[13]/div[3]/button[1]').click()
print('跳转提交支付')
sleep(2)

target = driver.find_element_by_class_name("edit")
driver.execute_script("arguments[0].scrollIntoView();", target)  # 页面拖动到底部
sleep(2)

# driver.find_element_by_xpath('//*[@id="payment_97"]/span').click()  #paypal
# print('paypal')
driver.find_element_by_xpath('//*[@id="payment_152"]/span').click()  # western Union
print('western union')
# driver.find_element_by_xpath('//*[@id="payment_165"]/span').click() #credit card
# print('credit card')
driver.find_element_by_xpath('//*[@id="place-order-mbtn"]').click()
print('支付成功')
sleep(2)
title = driver.find_element_by_css_selector(".theme-text")
print('单号：',title.text)