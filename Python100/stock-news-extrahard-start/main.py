import datetime
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query?"
NEWS_URL = "https://newsapi.org/v2/everything?"
STOCK_FUNC = "TIME_SERIES_DAILY"
API_KEY = "X345NTQB8XJCJM1V"
params = {
    "function": STOCK_FUNC,
    "symbol": STOCK,
    "apikey": API_KEY,
}


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return month_days[month - 1]
    if is_leap(year):
        return 29
    return 28


def get_day_before(year, month, day):
    if day > 1:
        return day - 1
    return days_in_month(year, month - 1)


response = requests.get(STOCK_URL, params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

today_date = datetime.date.today()
today_year = today_date.year
today_month = today_date.month
# today_day = today_date.day
today_day = 20          # test code
yest = get_day_before(today_year, today_month, today_day)
day_before_yest = get_day_before(today_year, today_month, yest)
yest_close_price = "0"
day_b4_yest_price = "0"

for date in data:
    if date == f"{today_year}-{today_month}-{yest}":
        yest_close_price = float(data[date]["4. close"])
    elif date == f"{today_year}-{today_month}-{day_before_yest}":
        day_b4_yest_price = float(data[date]["4. close"])

change_percent = (yest_close_price - day_b4_yest_price) / day_b4_yest_price * 100
print(change_percent)
if abs(change_percent) > 5:
    NEWS_API_KEY = "7f70dd8fdd654adfba1e4cdccfc0b59e"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_URL, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_articles = news_data["articles"][:3]

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    formatted_articles = [f"Headline: {article['title']},\nBrief: {article['description']}" for article in top_articles]
    for a in formatted_articles:
        print(a)
        print()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
