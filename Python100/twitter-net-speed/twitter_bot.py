import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

SPEEDTEST_URL = "https://www.speedtest.net/"
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_opt)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        sleep(5)
        go_button = self.driver.find_element(By.CSS_SELECTOR,
                                             'a[aria-label="start speed test - connection type multi"]')
        go_button.click()
        sleep(70)

        down_element = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.down = float(down_element.text)
        up_element = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = float(up_element.text)

    def tweet_at_provider(self, acc_name, acc_pass):
        self.driver.get("https://twitter.com/")
        sleep(2)
        sign_in = self.driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
        sign_in.click()
        sleep(2)
        input_name = self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
        input_name.send_keys(acc_name)
        input_name.send_keys(Keys.ENTER)
        input("Press Enter when finished with verification")
        sleep(2)
        input_pass = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        input_pass.send_keys(acc_pass)
        input_pass.send_keys(Keys.ENTER)
        sleep(2)
        text_box = self.driver.find_element(By.CSS_SELECTOR, 'div[contenteditable]')
        msg = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for"
               f" {PROMISED_DOWN}down/{PROMISED_UP}up?")
        text_box.send_keys(msg)
        sleep(1)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
        tweet_button.click()
