from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]") # find element by name("q")name = q yerine copy xpath yapabiliriz. search kısmında
time.sleep(1)

searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
# print(result)
result = driver.find_elements_by_css_selector(".repo-list-item .mt-n1 .text-normal a")

for element in result:
    print(element.text)

driver.close()