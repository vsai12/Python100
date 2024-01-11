from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.python.org"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_frac = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_whole}.{price_frac}")

# search_bar = driver.find_element(By.NAME, value="q")
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

html_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")
events = {ind: {"time": event.text.split("\n")[0], "name": event.text.split("\n")[1]}
          for ind, event in enumerate(html_events)}
print(events)

# driver.close()  # Closes tab
driver.quit()  # Closes browser
