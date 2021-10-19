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

def scrapping(page,genre):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    url = f'https://www.imdb.com/search/title/?genres={genre}&start={page}&explore=title_type,genres&ref_=adv_nxt'
    r = requests.get(url, headers=headers)

    htmlContent=r.content

    bs=BeautifulSoup(htmlContent,"html.parser")
    indented=bs.prettify()

    movies=bs.find_all ("div", class_="lister-item mode-advanced")

    # Attributes to Scrap
    years=[]
    duration=[]
    votes=[]
    genre=[]
    ratings=[]
    names=[]
    certificate=[]
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
    print ("Page Scrapped, Heading towards Next page")


# Driver Code
i=1
while i<=100000:
    scrapping(i,"sci-fi")
    i=+50

time = randint(2, 10)
sleep(time)

i=1
while i<=100000:
    scrapping(i,"comedy")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"action")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"romance")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"drama")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"thriller")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"romance")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"mystery")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"crime")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"animation")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"adventure")
    i=+50
time = randint(2, 10)
sleep(time)
i=1
while i<=100000:
    scrapping(i,"fantasy")
    i=+50