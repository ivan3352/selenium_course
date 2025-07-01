import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

link = 'http://suninjuly.github.io/redirect_accept.html'


def browser_init():
    browser_options = Options()
    browser_options.add_argument('--user-data-dir=/home/ivan/Downloads/selenium_course')
    return webdriver.Chrome(browser_options)


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


def button_click(browser):
    return browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


try:
    browser = browser_init()
    browser.get(link)
    button_click(browser)
    browser.switch_to.window(browser.window_handles[1]) #switching to a new tab
    number = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(number)
    button_click(browser)


finally:
    time.sleep(15)
    browser.quit()
