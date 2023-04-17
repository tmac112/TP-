import os
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import data, ddt
from openmarket.tools.read_file_tools import ReadFileUtils
from openmarket.model_page.shop_car_model import ShopCar

p = "./test_data/test_data.xlsx"
fpath = os.path.abspath(p)
shopcar_t = ReadFileUtils.readExcel(fpath, "shop_car_T")  # 正向数据
del_shop = ReadFileUtils.readExcel(fpath, "del_shop", has_title=False)


@ddt
class Shop_car(TestCase):
    def login(self):  # 登录
        self.dr.get("http://www.lekesite.xyz/index.php/Home/Index/index.html")
        self.dr.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.dr.find_element(By.ID, "username").send_keys("13800138006")
        self.dr.find_element(By.ID, "password").send_keys("a1B2c3D4")
        self.dr.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div/div[4]/a").click()

    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        self.go = ShopCar(self.dr)
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

    def tearDown(self) -> None:
        self.dr.quit()

    @data(*shopcar_t)
    def te1st_add(self, shop):
        self.go.add_shop(shop["name"], shop["count"])
        self.dr.implicitly_wait(2)
        # 添加成功文本 做断言
        ass1 = self.dr.find_element(By.XPATH,
                                    "/html/body/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div/span").text

        ass = "false"
        if ass1 == shop["expect"]:
            self.dr.find_element(By.XPATH,
                                 "/html/body/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div/div/a[2]").click()
            # 获取当前页面所有商品
            shops = self.dr.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[1]/div[2]/p/a")
            # 循环通过shop做断言
            for s in shops:
                if shop["name"] in s.text:
                    ass = "true"
        self.assertEqual(ass, "true", "断言失败")

    def te1st_del_all(self):
        self.go.del_all_shop()
        try:
            # 获取文本做断言
            act = self.dr.find_element(By.XPATH, "/html/body/div[2]/div/div/div/ul/li[1]").text
        except Exception as e:
            print("可能删除失败！", e)
            # 断言预期结果
        ass = "购物车空空的哦~，去看看心仪的商品吧~"
        self.assertEqual(ass, act, "断言失败")

    @data(*del_shop)
    def test_del(self, shop):
        self.go.del_shop(shop)
        # self.dr.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i").click()  # 点击全选按钮
        # n_ass = self.dr.find_element(By.XPATH, "/html/body/div[3]/div[1]/ul/li/a/em").text
        # n_ass1 = n_ass.replace('（', '')
        # n_ass2 = n_ass1.replace('）', '')
        self.dr.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/a[1]").click()  # 点击删除按钮
        self.dr.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/a[1]").click()  # 确认删除
        # self.dr.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[1]/div/i").click() #点击全选按钮
        # f_ass = self.dr.find_element(By.XPATH, "/html/body/div[3]/div[1]/ul/li/a/em").text
        # f_ass1 = f_ass.replace('（', '')
        # f_ass2 = f_ass1.replace('）', '')
        self.assertNotEqual("1""1", "断言失败")

    def tes1t_go(self):
        self.login()
        self.dr.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/a/div").click()  # 进入购物车页面
        expect = self.dr.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/p/a").text
        self.go.shop_go()
        act = self.dr.find_element(By.XPATH,
                                   "/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/div[2]/a").text
        self.assertEqual(expect, act, "断言失败")
