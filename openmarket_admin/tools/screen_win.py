import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import ImageGrab
# 获取全屏截图

def sava_screnn_window(driver):
    driver.save_screenshot("photos/%s.png" % time.strftime('%Y-%m-%d %H-%M-%S'))


# 指定元素截图
def get_ele_screen(element):
    element.screenshot("photos/%s.png" % time.strftime('%Y-%m-%d %H-%M-%S'))


def position_screen(x,y,x2,y2):
    position = (x,y,x2,y2)
    img = ImageGrab.grab(position)
    img.save("photos/%s.png" % time.strftime('%Y-%m-%d %H-%M-%S'))

# if __name__ == '__main__':