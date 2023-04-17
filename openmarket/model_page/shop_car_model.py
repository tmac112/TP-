import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.common.action_chains import ActionChains
import re
from openmarket.model_page.base_page import BasePage


class ShopCar(BasePage):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()  # 需注释

    def login(self):
        self.driver.get("http://www.lekesite.xyz/index.php/Home/Index/index.html")
        self.click((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/a[1]"))
        self.send_keys((By.ID, "username"), "13800138006")
        self.send_keys((By.ID, "password"), "a1B2c3D4")
        self.click((By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div/div[4]/a"))

    def add_shop(self, name, count):
        self.login()
        # 定位搜索框并搜索
        self.send_keys((By.ID, "q"), name)
        self.click((By.XPATH, "/html/body/div[2]/div/div[3]/ul/li[5]/form/a"))
        # 选择加购商品的数量
        self.clear_sendkey((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[1]/input"), count)

        self.click((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]/a"))
        # 切换到内嵌页
        self.driver.switch_to.frame("layui-layer-iframe1")

    def del_all_shop(self):
        self.login()
        self.click((By.XPATH, "/html/body/div[2]/div/div[4]/a/div"))  # 进入购物车界面
        all = self.local(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i").is_selected()
        # 检查是否全选，取消物品选中
        if not all:
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/a[1]"))
            self.click((By.ID, "removeGoods"))
            time.sleep(1)

    def del_shop(self, name):
        self.login()
        self.click((By.XPATH, "/html/body/div[2]/div/div[4]/a/div"))  # 进入购物车界面
        all = self.local(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i").is_selected()  # 检查是否全选
        # 同上
        if not all:
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
        else:
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))

        car = self.local(By.ID, "tpshop-cart")

        for e in name:
            goods_a = self.local(By.PARTIAL_LINK_TEXT, e)
            # 获取超链接的href属性
            goods_url = goods_a.get_attribute("href")
            # 获取超链接中商品的id
            num = re.findall("id/(.*?).html", goods_url)[0]
            # 根据商品id定位到可以点击的i标签
            i_obj = car.find_element(By.XPATH, f'//i[@data-goods-id="{num}"]')
            i_obj.click()  # i标签点击后复选框会有响应操作
            # obj = car.find_element(By.PARTIAL_LINK_TEXT, e)
            # ActionChains(self.driver).move_to_element(obj).perform()
            # ActionChains(self.driver).move_by_offset(-240, -5).click().perform()

    def shop_go(self):
        all = self.local(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i").is_selected()  # 检查是否全选
        #同上
        if all is True:
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
        else:
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
            time.sleep(0.2)
            self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/i"))
        self.click((By.XPATH, "/html/body/div[3]/div[3]/div[1]/div/div/div[1]/div[1]/i"))  # 选择第一个商品
        time.sleep(1)
        self.click((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a"))  # 点击结算
        self.driver.switch_to.alert.accept()
        self.click((By.ID, "submit_order"))  # 点击提交订单
        time.sleep(3)
        self.click((By.XPATH, "/html/body/div[1]/div/div/div/a[1]"))  # 点击跳转到个人首页
