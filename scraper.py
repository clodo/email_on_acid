import scraperwiki

from datetime import datetime
from bs4 import BeautifulSoup

url = "http://status.emailonacid.com/"

html = scraperwiki.scrape(url)
soup = BeautifulSoup(html, 'html.parser')

status = soup.h1.text
todays_date = str(datetime.now())

scraperwiki.sqlite.save(unique_keys=['date'], data={"status": status, "date": todays_date})
print status
