import requests
from bs4 import BeautifulSoup


def write_player_data_to_file(file):
    '''
    @description: reads data from html-paragraph and writes it in a txt-file
    @parameter: file to write data (dont need to be a string)
    '''

    filepointer = open(str(file), "a")

    links = set()
    result = requests.get("https://www.bundesliga.com/en/bundesliga/player")
    soup = BeautifulSoup(result.content, "html.parser")
    for a in soup.find_all('a', href=True):
       if "player" in a['href']:
           links.add(a['href'])

    for link in links:
        filepointer.write("\n")
        filepointer.write(link)
        result = requests.get("https://www.bundesliga.com" + link)
        soup = BeautifulSoup(result.content, "html.parser")
        for entry in soup.find_all("p", class_="vitaparagraph ng-star-inserted"):
            for part in entry.text.split("for "):
                if "from" in part:
                    filepointer.write(str(part.split(" from ")))
            break