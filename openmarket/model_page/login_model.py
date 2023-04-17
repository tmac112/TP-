from selenium import webdriver
from selenium.webdriver.common.by import By
from openmarket.model_page.base_page import BasePage

class Login(BasePage):
    def start(self):
        self.driver.get("http://www.lekesite.xyz/index.php/Home/Index/index.html")

    def login(self,name,pwd):
        self.start()
        self.click((By.XPATH,"/html/body/div[1]/div[1]/div/div/div[2]/a[1]"))
        self.send_keys((By.ID,"username"),name)
        self.send_keys((By.ID,"password"),pwd)
        self.click((By.XPATH,"/html/body/div[2]/div/div[2]/div/form/div/div[4]/a"))