import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # Нажать на кнопку
    browser.find_element_by_tag_name("button").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # считываем значение x
    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    # считаем функцию от х
    y = calc(x)
    # находим поле для ввода и вводим значение y
    browser.find_element_by_id("answer").send_keys(f"{y}")
    # находим кнопку и нажимаем
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
