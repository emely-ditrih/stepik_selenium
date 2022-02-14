import time
import  os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # заполняем поля
    name = browser.find_element_by_name("firstname")
    name.send_keys("name")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("lastname")
    email = browser.find_element_by_name("email")
    email.send_keys("@")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'empty.txt')

    # загружаем файл
    send_file = browser.find_element_by_id("file")
    send_file.send_keys(f"{file_path}")

    # нажимаем кнопку
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
