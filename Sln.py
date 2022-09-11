from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import os
import sys


username = "USERNAME"
password = "PASSWORD"


driver = webdriver.Firefox()


driver.get("https://www.tradingview.com")


driver.maximize_window()


driver.find_element(By.CLASS_NAME, 'tv-header__user-menu-button').click()
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@data-name="header-user-menu-sign-in"]'))).click()
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'js-show-email'))).click()
time.sleep(3)


driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'tv-button--loader').click()
time.sleep(3)


WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[starts-with (@class, "searchText")]'))).click()
driver.find_element(By.XPATH, '//input[starts-with (@name, "query")]').send_keys("ADAUSDT")
driver.find_element(By.XPATH, '//input[starts-with (@name, "query")]').send_keys(Keys.ENTER)

time.sleep(5)

WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@data-name="open-indicators-dialog"]'))).click()
driver.find_element(By.XPATH, '//input[@data-role="search"]').send_keys("WMX_Q AutoTrendlines")
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[starts-with (@class, "highlighted")]'))).click()
#WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[starts-with (@class, "close-button")]'))).click()
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[starts-with (@data-name, "close")]'))).click()

driver.save_screenshot("adaust.screnshot.png")
driver.back()

time.sleep(5)

WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[starts-with (@class, "searchText")]'))).click()
driver.find_element(By.XPATH, '//input[starts-with (@name, "query")]').send_keys("BTCUSDT")
driver.find_element(By.XPATH, '//input[starts-with (@name, "query")]').send_keys(Keys.ENTER)

time.sleep(5)

driver.save_screenshot("BTCUSDT.png")

time.sleep(5)

driver.back()

driver.close