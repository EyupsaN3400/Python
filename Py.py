from selenium import webdriver
import time

driver = webdriver.Chrome()



url = "https://github.com/EyupsaN3400"
driver.get(url)


time.sleep(3)

driver.maximize_window()
driver.save_screenshot("gihthub.com-homepage.png")


url = "http://github.com/Dyrnade"
driver.get(url)



print(driver.title)
if "EyupsaN3400" in driver.title:
    driver.save_screenshot("github-EyupsaN3400.png")


time.sleep(5)

driver.back()
#driver.forward

time.sleep(5)

driver.close()

