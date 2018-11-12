import requests                          # the module needed to request data from websites
from bs4 import BeautifulSoup            # the module needed to deal with data from a website

def links_collection(max_prognum):
    prognum = 600
    while prognum <= max_prognum:
        url = "#########################" + str(prognum)             # put a url here
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for item in soup.findAll("span", {"class": "long-txt-span"}):
            title = item.string
            print(title)

        for item in soup.findAll("a", {"class": "download axc"}):
            link = item.get("href")

            print(link)
            prognum +=1

links_collection(610)