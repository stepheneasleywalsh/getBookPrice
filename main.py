import requests
from bs4 import BeautifulSoup

def getPrice(url):
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, 'html.parser')
    x = soup.find("span", class_="sale-price")
    x = x.get_text()
    return(x)

def getLink(name):
    BOOK = name.replace(" ", "+")
    url = "https://www.bookdepository.com/search?searchTerm="+BOOK+"&search=Find+book"
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")
    block = str(soup.find("div", class_="content-block"))
    soup2 = BeautifulSoup(block, "html.parser")
    el = soup2.find(href=True)
    link = "https://www.bookdepository.com" + str(el['href'])
    return(link)

try:
    booktitle = input("Give me the name of a book: ")
    price = getPrice(getLink(booktitle))
    print(price)
except:
    print("No book found")

quit()