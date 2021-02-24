import requests
from bs4 import BeautifulSoup as bs

# Load the content
r = requests.get("https://www.youtube.com/watch?v=GjKQ6V_ViQE&ab_channel=KeithGalli.html")

# Convert to beautiful soup object
soup = bs(r.content,"html.parser")

heading = soup.find("svg")
# Print out the html
# print(heading.prettify())

ytd_app = soup.find("ytd-app")
tags = soup.find_all("ytd-app")
for t in tags:
    container = ytd_app.find("div", attrs={"id": "content"})
if(container):
    ytd_page_manager = container.find("ytd_page_manager", attrs={"id": "page-manager"})
    print(ytd_page_manager)

# Search
string_search = soup.find_all("yt-formatted-string", string="Comprehensive")
# print(string_search)

# Using regex
import re
string_search = soup.find_all("yt-formatted-string", string=re.compile("Comprehensive"))

# Using select
content = soup.select("ytd-app div#content")
print(content)

print (soup.body)