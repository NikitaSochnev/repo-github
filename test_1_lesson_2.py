from appium import webdriver
import pytest as pt
import appium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions
import time

desired_caps = {
    "deviceName": "Pixel_3a_API_30_x86",
    "platformName": "Android",
    "automationName" : "Appium",
    "version" : "11.0",
    "appPackage" : "org.wikipedia",
    "appActivity" : "main.MainActivity",
    "app" : "C:/PycharmProjects/test_home_work/app/org.wikipedia.apk"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

el = driver.find_element_by_xpath("//*[@text='Поиск по Википедии']")
el.click()
