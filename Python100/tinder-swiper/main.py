from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

FB_EMAIL = "ddwpk110@gmail.com"
FB_PASSWORD = "go1202"

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_opt)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
pass_input = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
fb_login = driver.find_element(By.CSS_SELECTOR, 'input[name="login"]')
email_input.send_keys(FB_EMAIL)
pass_input.send_keys(FB_PASSWORD)
fb_login.click()

driver.switch_to.window(base_window)




