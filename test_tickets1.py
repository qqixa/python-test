# -*- coding: utf-8 -*-
# _author_ = "qqx"
# date : 4/7/2020

from time import sleep
import cv2
import numpy as np
from selenium import webdriver
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'G:\python\tesseract-ocr\tesseract.exe'
# from test_login import login
# login()
# import test_login
# test_login.login()
class Test:
    def __init__(self, proxy='--proxy-server=socks5://192.168.1.42:55551'):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument(proxy)
        self.driver = webdriver.Chrome(chrome_options = self.option)
        self.driver.maximize_window()   # 窗口最大化
        timeout = 30
        self.driver.implicitly_wait(timeout)


    def login(self, account, passwd):
        self.driver.find_element_by_id('login_register_li').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="_email"]').click()
        self.driver.find_element_by_xpath('//*[@id="_email"]').send_keys(account)
        self.driver.find_element_by_id('_password').send_keys(passwd)
        self.driver.find_element_by_class_name('sign-btn').click()
        sleep(2)

    def get_verifyImg(self):
        self.driver.save_screenshot('tmp_screenshot.png')  # 截取整个页面
        pic = cv2.imread('tmp_screenshot.png', cv2.IMREAD_GRAYSCALE)
        #care = pic[30:60, 295:385]
        #care = pic[340:380,570:670]
        care = pic[341:381, 570:665]
        return care

    def Deal_with_verifyImg(self, img):
        care = cv2.medianBlur(img, 3)  # 中值滤波
        ret, th3 = cv2.threshold(care, 50, 255, cv2.THRESH_BINARY)  # 二值化
        pic_split = []
        for index in range(5):  # 切割
            pic_split.append(th3[:, index * 19: 19 + index * 19])
        afer_move = []
        for index in pic_split:  # 位移
            imgs = index
            while imgs[-7:-6, :].sum() <= imgs[-8:-7, :].sum():
                imgs = np.concatenate((imgs[-1:, :], imgs[:-1, :]))
            afer_move.append(imgs)
        image = np.concatenate(afer_move, axis=1)  # 组合

        return pytesseract.image_to_string(image, lang='eng')  # 识别

    def Func_ticket1(self):             ###### tictet入口1：详情页Email us ######
        self.driver.get('https://www.jjshouse.com/-g105575')
        sleep(2)
        self.login(account='qwe1@tetx.com', passwd='123456')
        mouse = self.driver.find_element_by_link_text('Ask a question')
        webdriver.common.action_chains.ActionChains(self.driver).move_to_element(mouse).perform()
        self.driver.find_element_by_link_text('Email us').click()
        print('ticket界面')

        self.handles = self.driver.window_handles
        self.driver.switch_to.window(self.handles[1])
        self.driver.find_element_by_xpath('//*[@id="form_question"]/ul/li[3]/div/label[3]').click()  # topic
        self.driver.find_element_by_id('comment_title').click()  # Question Title
        self.driver.find_element_by_id('comment_title').send_keys('test')
        self.driver.find_element_by_id('comment_content').click()  # Question
        self.driver.find_element_by_id('comment_content').send_keys('testTEST123@$%!')

        target = self.driver.find_element_by_class_name("trust")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 页面拖动到底部

        verifyImg = self.get_verifyImg()
        verifycode = self.Deal_with_verifyImg(verifyImg)
        print(f"OCR result: {verifycode}")
        self.driver.find_element_by_xpath('//*[@id="genCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="genCode"]').send_keys(verifycode)
        self.driver.find_element_by_id('sbmt_comment').click()     #提交ticket
        # sleep(1)
        # dig_confirm = self.driver.switch_to.alert     #切换到alert弹窗
        # sleep(1)
        # print('alert text:'+ dig_confirm.text)
        # dig_confirm.accept()  # 点击“确认”按钮
        # sleep(1)

    # def Func_ticket2(self):             ###### ticket入口2；订单待付款product support ######
    #     #self.driver.get('https://www.jjshouse.fr/account/order.php?order_sn=6401552446')
    #     #self.login(account='qwe1@tetx.com', passwd='123456')
    #     pass



if __name__ == '__main__':
    thistest = Test()
    thistest.Func_ticket1()
    #thistest.Func_ticket2()