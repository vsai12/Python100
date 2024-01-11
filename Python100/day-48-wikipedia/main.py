from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

URL = "https://en.wikipedia.org/wiki/Main_Page"
SIGN_UP_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_opt)
driver.get(SIGN_UP_URL)

# html_num_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# num_articles = int(html_num_articles.text.replace(",", ""))
# print(num_articles)
# html_num_articles.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python" + "\n")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
f_name.send_keys("Tetsuya")
l_name.send_keys("Kagami")
email.send_keys("ddwpk110@gmail.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.click()

# driver.quit()
