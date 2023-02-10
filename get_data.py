from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/List_of_ethnic_slurs'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text)

movie_list = soup.find_all('table', attrs={'class': "wikitable"})


def write(list):
    with open("data.txt", 'a') as f:
        f.write(list)
        f.write('\n')
list = []

for movie in movie_list:
    df = pd.read_html(str(movie))[0]
    terms = df["Term"]
    # print(terms)

    for t in terms:

      if "/" in t:
        list = t.split("/")
        for item in list:
          try:
            list.append(item.strip())

            # write(item.strip())
          except:
            None
      if "," in t:
        list = t.split(",")
        for item in list:
          try:
            list.append(item.strip())
            # write(item.strip())
          except:
            None
