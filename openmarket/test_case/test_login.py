import os
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import data, ddt
from openmarket.tools.read_file_tools import ReadFileUtils
from openmarket.model_page.login_model import Login

p = "./test_data/test_data.xlsx"
fpath = os.path.abspath(p)
login_t = ReadFileUtils.readExcel(fpath, "login_T")  # 正向数据
login_f = ReadFileUtils.readExcel(fpath, "login_F")  # 反向数据


@ddt
class Login_test(TestCase):
    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        self.lg = Login(self.dr)
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)


    def tearDown(self) -> None:
        self.dr.quit()

    @data(*login_t)
    def test_login_T(self, user):
        self.lg.login(user["name"], user["pwd"])
        expect = user["expect"]
        time.sleep(1)
        act = self.dr.current_url
        self.assertEqual(expect, act, f"断言失败,实际结果{act},期望{expect}")
    @data(*login_f)
    def tes1t_login_F(self, user):
        self.lg.login(user["name"], user["pwd"])
        expect = user["expect"]
        act = self.dr.find_element(By.XPATH, "/html/body/div[6]/div[2]").text
        self.assertEqual(expect, act, f"断言失败,实际结果{act},期望{expect}")

