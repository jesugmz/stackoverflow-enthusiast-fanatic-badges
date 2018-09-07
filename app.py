import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xvfbwrapper import Xvfb

LOGIN_PAGE = 'https://stackoverflow.com/users/login'


def start_driver():
    display = Xvfb(
        width=os.environ.get('SCREEN_WIDTH'), height=os.environ.get('SCREEN_HEIGHT'),
        colordepth=os.environ.get('SCREEN_DEPTH'))
    display.start()

    return display, webdriver.Firefox()


def login(driver, email, password):
    driver.get(LOGIN_PAGE)

    try:
        WebDriverWait(driver, 6, 0.2).until(EC.presence_of_element_located((By.ID, 'login-page')))
    except Exception:
        # todo: handle exception
        raise Exception

    email_input = driver.find_element_by_id('email')
    email_input.send_keys(email)

    password_input = driver.find_element_by_id('password')
    password_input.send_keys(password)

    password_input.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 6, 0.2).until(EC.url_to_be('https://stackoverflow.com/'))
    except Exception:
        # todo: handle exception
        raise Exception

    return driver.get_cookies()


def close_driver(display, driver):
    driver.quit()
    display.stop()


if __name__ == "__main__":
    # todo: add application logs
    display, driver = start_driver()
    # todo: save cookie to reuse it instead
    cookie = login(driver, os.environ.get('EMAIL'), os.environ.get('PASSWORD'))
    driver.get_screenshot_as_file('logged.png')
    close_driver(display, driver)
