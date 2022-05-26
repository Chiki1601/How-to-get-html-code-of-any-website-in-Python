import requests
from bs4 import BeautifulSoup
url ='https://google.com'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())
#print(page.content)
#print(status_code)
#print(page.encoding)
