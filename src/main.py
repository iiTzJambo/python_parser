import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 
from translate import Translator
from docx import Document
from getLinksFromTxt import links
from getDataFromLink import getPersonData

print(links)

personsList = []

for link in links:
    person = getPersonData(link)
    personsList.append(person)

ua = UserAgent() 
headers = {"User-Agent": ua.random} 

translator = Translator(to_lang="ru")
 






