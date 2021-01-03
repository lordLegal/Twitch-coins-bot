import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
browser.get("Link")  # Link

while Login == True:
    try:
        time.sleep(10)
        browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/button/div/div/div/div").click()
        u = browser.find_element_by_id("login-username")
        u.send_keys("Username")  # Username

        p = browser.find_element_by_id("password-input")
        p.send_keys("Password")  # Password

        browser.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div[3]/form/div/div[3]/button").click()
        print("[Server]need a 2fa code")
        af = str(input())
        f = browser.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div/input")
        f.send_keys(af)
        Login = False
        print("[Server]Logged in...")
        print("[Server]Starting...")
        print("[Server]wait for coins...")
        coins = True
        time.sleep(60)
    except NoSuchElementException:
        print("[Server]NoSuchElementException")
    except TimeoutException:
        print("[Server]TimeoutException")

while coins == True:
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button"))).click()
        print("[Server]coins got...")
        a = browser.find_element_by_xpath(
            "//*[@id='3c28396c0c3a7841c4e847c4c4bd8bf1']/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/button/div/div/div/div[2]/span").text
        print("[Server]coins now at  " + a)
    except NoSuchElementException:
        print("[Server]NoSuchElementException")
    except TimeoutException:
        pass
