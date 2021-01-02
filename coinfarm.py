import pickle
import smtplib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Login = True
coins = False

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get("URL")

while Login == True:
    time.sleep(5)
    browser.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/button/div/div/div/div").click()
    u = browser.find_element_by_id("login-username")
    u.send_keys("Username")

    p = browser.find_element_by_id("password-input")
    p.send_keys("Password")

    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div[3]/form/div/div[3]/button").click()
    Login = False
    coins = True
    time.sleep(120)

while coins == True:
    browser.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button").click()
    print("coins getet")
    time.sleep(900)
