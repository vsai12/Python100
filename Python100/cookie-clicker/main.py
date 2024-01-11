import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_opt)
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")


def is_browser_alive(d):
    try:
        temp = d.current_url
        return True
    except selenium.common.exceptions.WebDriverException:
        return False


purchase_time = time.time() + 5
time_out = time.time() + 60
while is_browser_alive(driver):
    cookie.click()
    if time.time() > purchase_time:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div[onclick]")
        store.pop()
        store.reverse()
        for item in store:
            cost = int(item.text.split("-")[1].split("\n")[0].replace(",", ""))
            curr_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            if curr_money > cost:
                item.click()
                break
        purchase_time = time.time() + 5
    if time.time() > time_out:
        break

cps = driver.find_element(By.ID, "cps")
print(cps.text)


