import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока элемент с id = "price" не станет равным 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    # price == 100 и нажимаем кнопку
    browser.find_element_by_id("book").click()

    # решить капчу для роботов, чтобы получить число с ответом
    # считываем значение x
    number = browser.find_element_by_id("input_value")
    x = int(number.text)
    # считаем функцию от х
    y = calc(x)
    # находим поле для ввода и вводим значение y
    browser.find_element_by_id("answer").send_keys(f"{y}")
    # находим кнопку и нажимаем
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(15)
    browser.quit()
