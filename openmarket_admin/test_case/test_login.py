import os
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import data, ddt
from openmarket.tools.read_file_tools import ReadFileUtils
from openmarket_admin.model_page.login_model import Login
from openmarket_admin.tools import screen_win


p = "./test_data/test_data.xlsx"
fpath = os.path.abspath(p)
login_t = ReadFileUtils.readExcel(fpath, "login_T")  # 正向数据
login_f = ReadFileUtils.readExcel(fpath, "login_F")  # 反向数据


@ddt
class login_Test(TestCase):
    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        self.lg = Login(self.dr)
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

    def tearDown(self) -> None:
        self.dr.quit()

    @data(*login_t)
    def tes1t_login_t(self, user):
        self.lg.login(user["name"], user["pwd"])
        # 获取当前网址做断言
        act = self.dr.current_url
        # screen_win.position_screen(500, 600, 1000, 1200)
        self.assertEqual(user["expect"], act, f"断言失败,实际结果是{act}")

    @data(*login_f)
    def test_login_f(self, user):
        self.lg.login(user["name"], user["pwd"])

        # 获取名称做断言
        act = self.dr.find_element(By.XPATH, "/html/body/div[1]/form/div/div[2]/span").text
        self.assertEqual(user["expect"], act, f"断言失败,实际结果是{act}")
