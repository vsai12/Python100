# import smtplib
#
# FROM_EMAIL = "ddwpk110@gmail.com"
# PASSWORD = "qaciryhayrxyldlz"
# TO_EMAIL = "Huangvincent00@gmail.com"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=FROM_EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg="Will is Fat")


import datetime as dt
import random
import smtplib

MY_EMAIL = "ddwpk110@gmail.com"
MY_PASS = "qaciryhayrxyldlz"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(MY_EMAIL,
                            MY_EMAIL,
                            f"Subject: Monday Motivation\n\n{quote}")
