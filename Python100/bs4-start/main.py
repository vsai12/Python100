from bs4 import BeautifulSoup
import requests

resp = requests.get("https://news.ycombinator.com/")
resp.raise_for_status()
yc_web_page = resp.text

soup = BeautifulSoup(yc_web_page, "html.parser")
all_a_tags = soup.find_all(name="a", rel="noreferrer")
a_texts = []
a_links = []
for a_tag in all_a_tags:
    a_text = a_tag.get_text()
    a_link = a_tag.get("href")
    a_texts.append(a_text)
    a_links.append(a_link)

a_votes = []
all_a_votes = soup.find_all(name="span", class_="score")
for a_vote in all_a_votes:
    votes = int (a_vote.get_text().split(" ")[0])
    a_votes.append(votes)

max_votes = a_votes[0]
max_ind = 0
for ind in range(1, len(a_votes)):
    if a_votes[ind] > max_votes:
        max_votes = a_votes[ind]
        max_ind = ind

print(f"{a_texts[max_ind]}, {a_links[max_ind]}, {a_votes[max_ind]}")


















# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)