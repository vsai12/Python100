from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLSfFIWR6S40Jv59cr9--GWtQVFEbsPW2Vxm4UckxWw2GN-hWiA/viewform?usp"
            "=sf_link")


resp = requests.get(ZILLOW_URL)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
all_listings = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
links = []
prices = []
address = []
for listing in all_listings:
    link = listing.a['href']
    price = listing.span.text.split("+")[0].split("/")[0]
    addr = listing.a.text.replace("|", ",").split(",", 1)[-1].strip()
    links.append(link)
    prices.append(price)
    address.append(addr)

driver = webdriver.Chrome()
driver.get(FORM_URL)

for ind in range(len(links)):
    sleep(3)
    addr_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr_input.send_keys(address[ind])
    price_input.send_keys(prices[ind])
    link_input.send_keys(links[ind])

    submit_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
    submit_button.click()
    sleep(3)

    submit_another = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_another.click()





