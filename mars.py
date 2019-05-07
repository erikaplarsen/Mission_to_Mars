from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import time

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
soup = bs(html, "html.parser")

article = soup.find('div', class_ = 'list_text')
news_title = article.find('div', class_='content_title').text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)

image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)

browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(3)
browser.click_link_by_partial_text('more info')

html = browser.html
soup = bs(html, 'html.parser')

featured_image = soup.find('figure', class_='lede').a['href']
featured_image_url = 'https://www.jpl.nasa.gov' + featured_image
print(featured_image_url)

weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)
html = browser.html
soup = bs(html, "html.parser")

tweet = soup.find('p',class_='TweetTextSize').text
tweet

facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
tables

usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(usgs_url)
html = browser.html
soup = bs(html, "html.parser")
hemispheres_dict = []


products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    hemispheres_dict.append({"title": title, "img_url": image_url})
    

print(hemispheres_dict)