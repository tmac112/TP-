import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from openmarket_admin.model_page.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Shop_admin(BasePage):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("http://www.lekesite.xyz/index.php/Admin/Admin/login")
        self.send_keys((By.NAME, "username"), "summer")
        self.send_keys((By.NAME, "password"), "Su1234mmer")
        self.click((By.NAME, "submit"))
        self.click((By.XPATH, "/html/body/div[1]/div[3]/ul/li[1]/a"))  # 进入首页
        self.driver.switch_to.frame("workspace")
        self.click((By.XPATH, "/html/body/div/div[1]/div[3]/div/a[1]"))  # 进入商品管理页面
        self.driver.switch_to.frame("workspace")  # 跳转到内嵌框架

    def shop_add(self, type, name, lei1, lei2, lei3, sale, market, date, model):
        self.login()
        self.click((By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]/a/div/span"))  # 点击添加商品
        if type == "1":  # 实物商品添加
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[2]/dd/input"), name)
            # 定位选择下拉框
            t1 = self.local(By.ID, "cat_id")
            Select(t1).select_by_visible_text(lei1)
            t2 = self.local(By.ID, "cat_id_2")
            Select(t2).select_by_visible_text(lei2)
            t3 = self.local(By.ID, "cat_id_3")
            Select(t3).select_by_visible_text(lei3)
            # 输入必选值
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[10]/dd/input"), sale)
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[11]/dd/input"), market)
            self.click((By.ID, "is_free_shipping_label_1"))  # 物流选择
            # 提交
            self.click((By.ID, "submit"))
        elif type == "2":  # 电子卡券添加
            self.click((By.XPATH, "/html/body/div[3]/form/div[1]/div/div/span[2]"))
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[2]/dd/input"), name)
            # 同上
            t1 = self.local(By.ID, "cat_id")
            Select(t1).select_by_visible_text(lei1)
            t2 = self.local(By.ID, "cat_id_2")
            Select(t2).select_by_visible_text(lei2)
            t3 = self.local(By.ID, "cat_id_3")
            Select(t3).select_by_visible_text(lei3)
            # 输入必选值
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[10]/dd/input"), sale)
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[11]/dd/input"), market)
            self.clear_sendkey((By.ID, "virtual_indate"), date)  # 电子卡券有效期
            self.click((By.ID, "submit"))
        elif type == "3":  # 预约商品
            self.click((By.XPATH, "/html/body/div[3]/form/div[1]/div/div/span[3]"))
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[2]/dd/input"), name)
            # 同上
            t1 = self.local(By.ID, "cat_id")
            Select(t1).select_by_visible_text(lei1)
            t2 = self.local(By.ID, "cat_id_2")
            Select(t2).select_by_visible_text(lei2)
            t3 = self.local(By.ID, "cat_id_3")
            Select(t3).select_by_visible_text(lei3)
            # 输入必选值
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[10]/dd/input"), sale)
            self.send_keys((By.XPATH, "/html/body/div[3]/form/div[1]/dl[11]/dd/input"), market)
            m = self.local(By.ID, "bespeak_template")
            Select(m).select_by_visible_text(model)  # 预约模板
            self.click((By.XPATH, "/html/body/div[3]/form/div[1]/dl[23]/dd/input[1]"))
            self.click((By.ID, "submit"))

    def del_shop(self, name):
        self.login()
        # 获取当前页面所有商品名称
        shops = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr/td[4]/div")
        # 循环要指定选中点击的商品
        for s in shops:
            if s.text in name:
                s.click()
                # 点击提交
        self.click((By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[3]/a/div/span"))
        self.click((By.XPATH, "/html/body/div[5]/div[3]/a[1]"))

    def view_shop(self):
        self.login()
        # 获取断言值通过名称
        expect = self.local(By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr[1]/td[4]/div").text
        # 定位点击
        self.move_to_element((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr[1]/td[2]/div/span/em"))
        self.click((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/table/tbody/tr[1]/td[2]/div/span/ul/li[1]/a"))
        # 切换到新打开窗口
        self.windows_1()

        return expect
