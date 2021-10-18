import pandas as pd
from random import randint
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
from bs4 import BeautifulSoup
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=SGRE2DQMR1KZRWZZDK4B&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_2'
options=Options()
exepath = 'G:\\Mid term Project\\CS261F21PID62\\\chromedriver.exe'
driver=webdriver.Chrome(options=options, executable_path=exepath)

driver.get(url)
driver.quit()
