import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# <editor-fold desc="Constants">
URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3749461921&f_AL=true&f_E=2&f_TPR=r86400&geoId=103644278"
       "&keywords=software%20engineer&location=United%20States&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
EMAIL = "Huangvincent00@gmail.com"
MY_PASS = "dragonewt1202"
MY_PHONE = "4084390898"


# </editor-fold>

def abort_application():
    c_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    c_button.click()

    time.sleep(2)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, value="username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(MY_PASS)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(MY_PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
