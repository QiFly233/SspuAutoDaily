"""
@author: QiFly
@version: v1.1
@date: 2021/05/09
"""

import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

name = [
    'name1', 'name2'
]
user = {
    'name1': 'IDNumbers1',
    'name2': 'IDNumbers2'
}
pwd = {
    'name1': 'password1',
    'name2': 'password2',
}
response_time = 300

class Sspu_auto():

    def __init__(self):
        url = 'http://hsm.sspu.edu.cn/selfreport/Default.aspx'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.driver.get(url)

    def login(self, id, passwd):

        username = self.driver.find_element(By.ID, 'username')
        username.send_keys(id)
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(0, 1))

        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(passwd)
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(0, 1))

        loginbutton = self.driver.find_element(By.CLASS_NAME, 'submit_button')
        loginbutton.click()
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(0, 1))

    def form_full(self, rddegree):
        dailybutton = self.driver.find_element(By.CLASS_NAME, 'icos')
        dailybutton.click()
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(0, 1))

        #promise = self.driver.find_element(By.ID, 'p1_ChengNuo-inputEl-icon')
        #promise.click()
        #time.sleep(random.randint(1, 3))

        health = self.driver.find_element(By.ID, 'fineui_2-inputEl-icon')
        health.click()
        time.sleep(random.randint(1, 2))

        good = self.driver.find_element_by_id('fineui_2-inputEl-icon')
        good.click()
        time.sleep(random.randint(1, 2))

        temperature = self.driver.find_element(By.ID, 'p1_TiWen-inputEl')
        temperature.send_keys(rddegree)
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(1, 2))

        forteen1 = self.driver.find_element_by_id('fineui_13-inputEl-icon')  # 点击否
        forteen1.click()
        time.sleep(random.randint(1, 2))

        forteen2 = self.driver.find_element_by_id('fineui_15-inputEl-icon')  # 点击否
        forteen2.click()
        time.sleep(random.randint(1, 2))

        inShanghai = self.driver.find_element_by_class_name('f-field-checkbox-switch-text.f-noselect')
        inShanghai.click()
        time.sleep(random.randint(1, 2))

        isAdress = self.driver.find_element_by_id('p1_CheckAddress-inputEl-icon')  # 确认精确地址
        isAdress.click()
        time.sleep(random.randint(1, 2))

        finalsumbit = self.driver.find_element(By.LINK_TEXT, '填写完毕，确认提交(Submit)')
        finalsumbit.click()
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(1, 2))

        correctsumbit = self.driver.find_element(By.LINK_TEXT, '确定')
        correctsumbit.click()
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(1, 2))

        confirm = self.driver.find_element(By.LINK_TEXT, '确定')
        confirm.click()
        self.driver.implicitly_wait(response_time)
        time.sleep(random.randint(3, 4))

    def quit(self):
        self.driver.quit()





def running():

    for dictname in name:
        degree = random.uniform(36.4, 36.8)  # 体温
        degree = round(degree, 1)
        degree = str(degree)

        cease_time = random.randint(2, 3)
        time.sleep(cease_time)

        #print(user[dictname])
        sspu = Sspu_auto()
        sspu.login(user[dictname], pwd[dictname])
        sspu.form_full(degree)
        sspu.quit()

        print('ok')


running()
