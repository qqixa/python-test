# -*- coding: utf-8 -*-
# _author_ = "qqx"
# date : 4/7/2020

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

def hover(self, by, value):  # 添加鼠标悬浮定位功能
    element = self.findElement(by, value)
    ActionChains(self.driver).move_to_element(element).perform()

def webdriver1():
    option = webdriver.ChromeOptions()
    option.add_argument('--proxy-server=socks5://192.168.1.42:55551')  # 浏览器代理配置
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

def add(driver):
    driver.get('https://www.jjshouse.com/cart.php')
    sleep(2)
    sum = driver.find_element_by_id('cart_item_total').text
    # sum = driver.find_element_by_xpath('//*[@id="cart_item_total"]').text
    print(sum)
    while sum != '( 0 Item )':  # 清空购物车
        driver.find_element_by_class_name('removeItem').click()
        # driver.find_element_by_xpath('//*[@id="item_41926743"]/td[4]/a').click()
        sleep(4)
        sum = driver.find_element_by_id('cart_item_total').text
        # sum = driver.find_element_by_xpath('//*[@id="cart_item_total"]').text
        print(sum)
        sleep(2)
    driver.get('https://www.jjshouse.com/-g4044')
    print('g4044')
    driver.find_element_by_id('_add_to_cart').click()
    print('加购成功')
    sleep(2)
    driver.find_element_by_id('shoppingCartGoodsTotal').click()
    print('跳转购物车页面')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="shopping-cart-float-right"]/a').click()
    print('跳转提交支付页面')
    sleep(2)

    target = driver.find_element_by_class_name("trust")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 页面拖动到底部
    sleep(2)

    # driver.find_element_by_id('payment-radio-97').click()  #paypal
    # print('paypal')
    driver.find_element_by_id('payment-radio-152').click()  # western Union
    print('western union')
    # driver.find_element_by_id('payment-radio-165').click()       #credit card
    # print('credit card')
    driver.find_element_by_xpath('//*[@id="btn_sbmt_order"]').click()
    print('支付成功')
    title = driver.find_element_by_css_selector(".theme-text")
    print('单号：', title.text)

if __name__ == '__main__':
    handle = webdriver1()
    login(driver=handle, account='qwe1@tetx.com',passwd='123456')
    add(driver=handle)
