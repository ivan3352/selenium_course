import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'


def browser_init():
    browser_options = Options()
    browser_options.add_argument('--user-data-dir=/home/ivan/Downloads/selenium_course')
    return webdriver.Chrome(browser_options)


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


def button_click(browser, id):
    return browser.find_element(By.ID, id).click()


try:
    browser = browser_init()
    browser.get(link)
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button_click(browser, 'book')
    number = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(number)
    button_click(browser, 'solve')

finally:
    time.sleep(15)
    browser.quit()
