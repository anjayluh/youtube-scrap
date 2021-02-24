import requests
from bs4 import BeautifulSoup as bs
# load web page
request = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = bs(request.content, "html.parser")
# print(soup.prettify)

# Grab all of the social links from the web page. Do it in three different ways
links = soup.select("link")
# print(links)
links_2 = soup.find_all("link")
# print(links_2)
links_3 = soup.select("ul li a", attrs={"href": "https://www.instagram.com/keithgalli/"})
actual_links = [link["href"] for link in links_3]
print(links_3)
# 