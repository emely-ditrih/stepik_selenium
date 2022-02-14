import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_tag_name("button")

    #скроллим страницу, что бы вывести кнопку из под баннера
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

finally:
    browser.quit()