import hashlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self, driver):
    #     self.driver = webdriver.Chrome()
        self.driver = driver  # 浏览器驱动

    # 定位标签用的工具
    def local(self, key, val):
        return self.driver.find_element(key, val)

    # 点击的工具方法
    def click(self, loc):
        self.local(*loc).click()

    # 向指定位置的标签发送数据
    def send_keys(self, loc, value):
        self.local(*loc).send_keys(value)

    # 将鼠标在指定标签上悬浮
    def move_to_element(self, loc):
        ele = self.local(*loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 清除再送值
    def clear_sendkey(self, loc, value):
        self.local(*loc).clear()
        self.local(*loc).send_keys(value)

    # 判断选中
    def selected(self, loc):
        return self.local(*loc).is_selected()

    # 获取打开的第一个新窗口
    def windows_1(self):
        w = self.driver.window_handles
        self.driver.switch_to.window(w[1])

    # 取消选中
    def clear_all(self,loc):
        all = self.local(*loc)  # 检查是否全选
        a = all.is_selected()
        if a is True:
            all.click()
        else:
            all.click()
            time.sleep(0.2)
            all.click()
# 解密文件md5
    def md5_file(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()