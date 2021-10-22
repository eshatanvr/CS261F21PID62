# Libraries to import:
# {
import pandas as pd
import warnings
import requests
warnings.filterwarnings("ignore", category=DeprecationWarning)
from bs4 import BeautifulSoup
from random import randint
from time import sleep
# }


# Attributes to Scrap
years = []
duration = []
votes = []
genre = []
ratings = []
names = []
certificate = []
count=0
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
url = 'https://www.imdb.com/search/title/?genres=comedy&start=1&explore=title_type,genres&ref_=adv_nxt'
while count<=24000:

    r = requests.get(url, headers=headers)

    htmlContent=r.content

    bs=BeautifulSoup(htmlContent,"html.parser")
    indented=bs.prettify()

    movies=bs.find_all ("div", class_="lister-item mode-advanced")
    nextbtn = bs.find('a', {'class': 'lister-page-next next-page'})['href']
    for items in movies:
        # For titles of the movie/show
        name = items.find('img', {'class':'loadlate'})['alt']
        names.append(name)

        # For the year of movie
        year=items.find('span',{'class':'lister-item-year text-muted unbold'}).text
        years.append(year)

        # For the time duration of movie
        try:
            time = items.find('span', {'class': 'runtime'}).text
        except:
            time="None"
        duration.append(time)

        # For the votes given to the show/movie
        try:
            vote = items.find('span', {'name': 'nv'}).text
        except:
            vote="None"
        votes.append(vote)

        # For the genre of the movie
        gen=items.find('span',{'class':'genre'}).text
        genre.append(gen)

        # For the ratings of the movie
        try:
            rate=items.find('strong').text
        except:
            rate="None"
        ratings.append(rate)

        #For the Certificate of the show
        try:
            cert = items.find('span', {'class': 'certificate'}).text
        except:
            cert="None"
        certificate.append(cert)

    Data = {'Title': names, 'Year': years, 'Duration': duration, 'Genre': genre, 'Certificate': certificate,
            'Ratings': ratings, 'Votes': votes}
    df = pd.DataFrame(Data)
    df.to_csv('MoviesData.csv', index=True, header=True)
    print("Page no.",count+1," scrapped")
    count+=1
    url="https://www.imdb.com"+nextbtn
