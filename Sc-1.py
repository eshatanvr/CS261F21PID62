# Libraries to import:
# {
import pandas as pd
import warnings
import requests
warnings.filterwarnings("ignore", category=DeprecationWarning)
from random import randint
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
from bs4 import BeautifulSoup
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# }

# Driver Code
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
url = 'https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=SGRE2DQMR1KZRWZZDK4B&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_2'
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

Data={'Title':names,'Year':years,'Duration':duration,'Genre':genre,'Certificate':certificate,'Ratings':ratings,'Votes':votes}
df=pd.DataFrame(Data)
df.to_csv('MoviesData.csv',index=True,header=True)