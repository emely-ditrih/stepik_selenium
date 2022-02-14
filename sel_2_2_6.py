import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # открываем сайт
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # считываем значение x
    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    # считаем функцию от х
    y = calc(x)
    # находим кнопку и скроллим страницу вниз, чтобы кнопка оказалась сверху
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # не работает((
    browser.execute_script("window.scrollBy(0, 100);") # скроллим на 100 пикселей вниз
    # находим поле для ввода и вводим значение y
    area_answer = browser.find_element_by_id("answer")
    area_answer.send_keys(f"{y}")
    # выбрать checkbox, переключить radiobutton, нажать кнопку
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()
    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()
