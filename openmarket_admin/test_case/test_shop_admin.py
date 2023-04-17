import os
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import data, ddt
from openmarket.tools.read_file_tools import ReadFileUtils
from openmarket_admin.model_page.shop_admin import Shop_admin

p = "./test_data/test_data.xlsx"
fpath = os.path.abspath(p)
add_t = ReadFileUtils.readExcel(fpath, "shop_add_T")  # 正向数据
add_f = ReadFileUtils.readExcel(fpath, "shop_add_F")  # 反向数据
del_t = ReadFileUtils.readExcel(fpath, "del_shop_T", has_title=False)


@ddt
class Admin_shop(TestCase):
    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        self.ad = Shop_admin(self.dr)
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

    def tearDown(self) -> None:
        self.dr.quit()

    @data(*add_t)
    def te1st_add_T(self, shop):
        self.ad.shop_add(shop["type"], shop["name"], shop["lei1"], shop["lei2"], shop["lei3"], shop["sale"],
                         shop["market"], shop["date"], shop["model"])
        time.sleep(2)
        # 获取文本做断言
        act = self.dr.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr[1]/td[4]/div").text
        self.assertEqual(act, shop["expect"], "断言失败")

    @data(*add_f)
    def tes1t_add_F(self, shop):
        self.ad.shop_add(shop["type"], shop["name"], shop["lei1"], shop["lei2"], shop["lei3"], shop["sale"],
                         shop["market"], shop["date"], shop["model"])
        # 同上
        act = self.dr.find_element(By.XPATH, '/html/body/div[6]/div').text
        self.assertEqual(act, shop["expect"], "断言失败")

    @data(*del_t)
    def tes1t_del_T(self, shop):
        self.ad.del_shop(shop[1:])
        time.sleep(0.5)
        # 同上
        act = self.dr.find_element(By.XPATH, '//*[@id="layui-layer2"]/div').text
        self.assertEqual(act, shop[0], "断言失败")

    def test_view_shop(self):
        expect = self.ad.view_shop()
        # 同上
        act = self.dr.find_element(By.XPATH, "/html/body/div[3]/div/form/div/h1").text
        # w = self.dr.window_handles
        # self.dr.switch_to.window(w[0])
        # self.dr.switch_to.frame("workspace")
        # expect = self.dr.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr[1]/td[4]/div").text
        # expect = self.ad.view_shop()
        self.assertEqual(expect, act, "断言失败")
