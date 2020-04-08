# -*- coding: utf-8 -*-
# _author_ = "qqx"
# date : 4/7/2020

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   #鼠标悬停
from PIL import Image,ImageEnhance
import pytesseract
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=socks5://192.168.1.42:55551')  # 浏览器代理配置
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()   # 窗口最大化

###################### 入口1：详情页Email us #############################
def TICKET1():
    driver.get('https://www.jjshouse.com/-g105575')
    driver.find_element_by_id('login_register_li').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="_email"]').click()  # 登录
    driver.find_element_by_xpath('//*[@id="_email"]').send_keys('qwe1@tetx.com')
    driver.find_element_by_id('_password').send_keys('123456')
    driver.find_element_by_class_name('sign-btn').click()
    print('登录成功')
    sleep(5)
    # driver.find_element_by_xpath('//*[@id="signOrLogin"]/div/h6/em').click()    #sign out
    # driver.find_element_by_xpath('//*[@id="signOrLogin"]/div/div/a[6]').click()
    # print('退出登录')

    mouse = driver.find_element_by_link_text('Ask a question')     #鼠标悬停才显示Email us
    ActionChains(driver).move_to_element(mouse).perform()
    sleep(2)
    driver.find_element_by_link_text('Email us').click()
    sleep(2)
    print('ticket界面')

    handles = driver.window_handles         # 获取当前浏览器全部窗口句柄
    driver.switch_to.window(handles[1])     # 切换到新标签页，n=1定位到当前浏览器的第二个标签页

    driver.find_element_by_xpath('//*[@id="form_question"]/ul/li[3]/div/label[3]').click()   # topic
    driver.find_element_by_id('comment_title').click()            # Question Title
    driver.find_element_by_id('comment_title').send_keys('test')
    driver.find_element_by_id('comment_content').click()            # Question
    driver.find_element_by_id('comment_content').send_keys('testTEST123@$%!')

    target = driver.find_element_by_class_name("trust")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 页面拖动到底部
    sleep(2)
    driver.save_screenshot('picture.png')  # 截取整个页面
    code1 = driver.find_element_by_id('verifyImg')
    # print(code1.location)
    sleep(2)
    # left = code1.location['x']               # 自动定位
    # top = code1.location['y']
    # right = code1.size['width'] + left
    # height = code1.size['height'] + top
    im = Image.open('picture.png')
    box = (570,340,670,380)          # 手动定位验证码位置
    im.crop(box).save('picture1.png')   # 保存获取的验证码
    # img = im.crop((left,top, right, height))
    # img.save('picture1.png')  # 截取到的验证码图片
    sleep(2)

    class demo():
        def __init__(self, path):
            self.image = Image.open(path)
            self.image = self.image.convert('L')

        def test(self):
            threshold = 50
            table = []
            for i in range(256):
                if i < threshold:
                    table.append(0)
                else:
                    table.append(1)
            self.image = self.image.point(table, '1')
            self.img_array = self.image.load()
            width = self.image.size[0]
            height = self.image.size[1]
            for i in range(0, 1000):
                for x in range(1, width - 1):
                    for y in range(1, height - 1):
                        count = 0
                        if self.img_array[x, y] == self.img_array[x - 1, y + 1]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x, y + 1]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x + 1, y + 1]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x - 1, y]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x + 1, y]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x - 1, y - 1]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x, y - 1]:
                            count += 1
                        if self.img_array[x, y] == self.img_array[x + 1, y - 1]:
                            count += 1
                        if count <= 2 and count > 1:
                            self.img_array[x, y] = 1

            self.image = self.image.convert('L')
            self.image.show()
            self.image.save('picture2.png')
            final = pytesseract.image_to_string(self.image)
            return final


    demo('picture1.png').test()
    verifycode = demo('picture1.png').test()
    print(verifycode)

    sleep(2)
    driver.find_element_by_xpath('//*[@id="genCode"]').click()
    driver.find_element_by_xpath('//*[@id="genCode"]').send_keys(verifycode)
    driver.find_element_by_id('sbmt_comment').click()

###################### 入口2：订单待付款product support #############################
def TICKET2():
    driver.get('https://www.jjshouse.fr/account/order.php?order_sn=6401552446')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="_email"]').click()                        #登录
    driver.find_element_by_xpath('//*[@id="_email"]').send_keys('qwe1@tetx.com')
    driver.find_element_by_id('_password').send_keys('123456')
    driver.find_element_by_class_name('sign-btn').click()
    sleep(2)
    print('待付款订单6401552446')
    driver.find_element_by_xpath('//*[@id="items_label_0"]/div[1]/div/div/a').click()
    print('跳转product support')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="my_form"]/div/div[2]/label/img').click()
    driver.find_element_by_id('_message').click()            # detail message
    driver.find_element_by_id('_message').send_keys('ABCabc123!@#$')
    driver.find_element_by_id('_phone').click()            # phone number
    driver.find_element_by_id('_phone').send_keys('12345678')
    driver.find_element_by_id('sbmit_frm_btn').click()     # submit
    sleep(2)
    driver.find_element_by_id('submit1').click()           # comfirm
    sleep(2)
    ordertext = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/ul/li[2]').text   # 获取文本
    ticketid = ''.join([x for x in ordertext if x.isdigit()])    # 文本中提取数字
    print('ticket id:',ticketid)
    sleep(2)
    driver.find_element_by_id('signOrLogin').click()
    driver.find_element_by_xpath('//*[@id="signOrLogin"]/div/div/a[4]').click()   # my ticket
    print('跳转my ticket')
    sleep(2)    
    ticketid1 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/table/tbody/tr[2]/td[2]/a').text
    if ticketid == ticketid1:
        print('提交成功')
    else:
        print('提交失败')

if __name__=="__main__":
       TICKET2()


