import selenium
from twitter_bot import InternetSpeedTwitterBot

TWITTER_EMAIL = "kagero1202@gmail.com"
TWITTER_PASS = "Leopald@1155"
TWITTER_USER = "BenTian29694766"

twitter_bot = InternetSpeedTwitterBot()
# twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASS)
twitter_bot.driver.quit()

