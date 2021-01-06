# -*- coding:utf-8 -*-
# @Time     :2021/1/6 2:10 下午
# @Author   :yun bosheng
# @File     :test_wecom.py
from time import sleep

import selenium
import pytest
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TestWeCom:
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        if len(open("cookie.json").read()) != 0:
            with open("cookie.json", "r") as f:
                    cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            sleep(3)
            try:
                expected_conditions.visibility_of(
                    (self.driver.find_element_by_id('menu_index')))
            except Exception:
                sleep(20)
                cookies = self.driver.get_cookies()
                with open("cookie.json", "w") as f:

                    json.dump(cookies, f)
                self.test_cookie()

            else:
                sleep(5)
                self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        else:
            cookies = self.driver.get_cookies()
            with open("cookie.json", "w") as f:
                json.dump(cookies, f)
            self.test_cookie()
