from selenium import webdriver
import time

driver = webdriver.Chrome()



url = "https://github.com/EyupsaN3400"



driver.get(url)

time.sleep(3)
print(driver.title)

driver.close()

