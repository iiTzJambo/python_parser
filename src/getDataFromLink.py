import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 

ua = UserAgent() 
headers = {"User-Agent": ua.random}

def getName(wrapper):
    name = wrapper.find("h1", class_ = "title").text
    return name

def getPhoto(wrapper):
    photo = wrapper.find("img", class_="img-responsive").get("src")
    return photo

def getBio(wrapper):
    bio = wrapper.find("div", class_="body").text
    return bio


def getPersonData(link):
    response = requests.get(link, headers = headers)
    soup = BeautifulSoup(response.text, "lxml")
    #wrapper = 

