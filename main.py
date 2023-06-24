from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

login = "Ваш логин"
password = "Ваш пароль"
text = "Hello World!"
searh_text = "Star Wars"

try:
    driver = webdriver.Chrome()
    driver.get("https://www.vk.com")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "index_email")
    email_input.send_keys(login)
    time.sleep(3)

    button1 = driver.find_element(
        By.XPATH, '//*[@id="index_login"]/div/form/button/span'
    ).click()
    time.sleep(3)

    password_input = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input',
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    message = driver.find_element(By.ID, "l_msg").click()
    time.sleep(3)

    start_dialog = driver.find_element(
        By.XPATH, '//*[@id="im_dialogs"]/li[1]/div[2]'
    ).click()
    time.sleep(3)

    message_text = driver.find_element(By.ID, "im_editable0")
    message_text.send_keys(text)
    message_text.send_keys(Keys.ENTER)
    time.sleep(5)

    search_area = driver.find_element(By.ID, "SearchTopInput")
    search_area.send_keys(searh_text)
    search_area.send_keys(Keys.ENTER)
    time.sleep(10)

    message = driver.find_element(By.ID, "l_msg").click()
    time.sleep(3)

    start_dialog = driver.find_element(
        By.XPATH, '//*[@id="im_dialogs"]/li[1]/div[2]'
    ).click()
    time.sleep(3)

finally:
    driver.close()
    driver.quit()
