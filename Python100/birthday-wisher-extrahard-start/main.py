import datetime as dt
import random
import smtplib

import pandas as pd

MY_EMAIL = "ddwpk110@gmail.com"
MY_PASS = "qaciryhayrxyldlz"

now = dt.datetime.now()
month = now.month
day = now.day

name = None
email = MY_EMAIL
df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if row.month == month and row.day == day:
        name = row['name']
        email = row['email']

letter_num = random.randint(1, 3)
with open(f"letter_templates/letter_{letter_num}.txt") as letter:
    data = letter.read()

data = data.replace("[NAME]", name)
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(MY_EMAIL,
                        email,
                        data)

