import requests
from bs4 import BeautifulSoup as bs
# load web page
request = requests.get("https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbngwamdicExVWEZicFRPdHM5b1BwUmJpRjlJUXxBQ3Jtc0tra1JEdGhpV2d4azV4NDM5QmNVVXp4TGNSRUNMVF9VWVhWc3AwX2RMME5KRURieFdtZzUzY1ZxU3kxcWVvR1M3bFZXckwxVUxuc3kxSXZhU3hsYmFvb3I2MkN2ak1pQTVaNmZnNlh4Q05FcEVUR2dmdw&q=https%3A%2F%2Fkeithgalli.github.io%2Fweb-scraping%2Fexample.html")
soup = bs(r.content, "html.parser")
soup