import smtplib

from bs4 import BeautifulSoup
import lxml
import requests

MY_EMAIL = "ddwpk110@gmail.com"
MY_PASS = "qaciryhayrxyldlz"
TARGET_PRICE = 100

PRODUCT_URL = ("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=dp_prsubs_sccl_3/141-7922247"
               "-1091745?pd_rd_w=xPXVx&content-id=amzn1.sym.097c27c2-82af-4eb5-99e0-a88579ba3622&pf_rd_p=097c27c2"
               "-82af-4eb5-99e0-a88579ba3622&pf_rd_r=81CRJQWM9T6E6DGZ3GYQ&pd_rd_wg=p0fVl&pd_rd_r=6cfea963-f1c2-4b85"
               "-a4b8-4531c11b3566&pd_rd_i=B01NBKTPTS&th=1")
TEST_URL = ("https://www.amazon.com/dp/B0BZS1D9R9/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0BZS1D9R9&pd_rd_w=zGVNv&content"
            "-id=amzn1.sym.386c274b-4bfe-4421-9052-a1a56db557ab&pf_rd_p=386c274b-4bfe-4421-9052-a1a56db557ab&pf_rd_r"
            "=4DA2358NA965XKTPJ625&pd_rd_wg=xb36r&pd_rd_r=9e09e69e-e26f-4cb3-9d74-0b852f30ff1b&s=kitchen&sp_csd"
            "=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}

resp = requests.get(TEST_URL, headers=header)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "lxml")
text_price = soup.find("span", class_="aok-offscreen").get_text()
price = float(text_price.split("$")[1].strip())
title = soup.find("span", id="productTitle").get_text().strip()
print(price)

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        msg = f"Subject:Amazon Price Alert!\n\n{title} is now ${price}\n{TEST_URL}".encode("utf-8")
        connection.sendmail(MY_EMAIL,
                            MY_EMAIL,
                            msg)

