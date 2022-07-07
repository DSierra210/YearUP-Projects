import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("./chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://myanimelist.net/topanime.php")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

anime_rankings = []
anime_titles = []
anime_scores = []

for ele in soup.findAll("td", class_="rank ac"):
    rank = ele.find("span")
    anime_rankings.append(rank.text)

for ele in soup.findAll("div", class_="di-ib clearfix"):
    title = ele.find("h3")
    anime_titles.append(title.text)

for ele in soup.findAll("div", class_="js-top-ranking-score-col di-ib al"):
    score = ele.find("span")
    anime_scores.append(score.text)

df = pd.DataFrame({"Rank": anime_rankings, "Title": anime_titles, "Score": anime_scores})
df.to_csv("Anime_list.csv", index=False, encoding="UTF-8")
