from selenium import webdriver
from selenium.webdriver.common.by import By
from openmarket_admin.model_page.base_page import BasePage


class Login(BasePage):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def login(self, name, pwd):
        # 打开网站输入用户名密码
        self.driver.get("http://www.lekesite.xyz/index.php/Admin/Admin/login")
        self.send_keys((By.NAME, "username"), name)
        self.send_keys((By.NAME, "password"), pwd)
        self.click((By.NAME, "submit"))

