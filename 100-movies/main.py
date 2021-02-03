from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     content = file.read()
#
#
# soup = BeautifulSoup(content, "html.parser")
# #print(soup.prettify())
# #print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a") #string is the CSS selector
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvote)

max_upvote = max(article_upvote)
print(max_upvote)

largest_index = article_upvote.index(max_upvote)

print(article_texts[largest_index])
print(article_links[largest_index])
