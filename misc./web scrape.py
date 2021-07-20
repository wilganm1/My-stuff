from bs4 import BeautifulSoup
from urllib.request import urlopen

url = #!!! insert url here
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.find_all(#tag)

image1, image2 = soup.find_all(#tag)

soup.title.string

soup.find_all("img", src="/static/dionysus.jpg")

