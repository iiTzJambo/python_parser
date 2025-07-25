import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin
from getLinksFromTxt import links

ua = UserAgent()
headers = {"User-Agent": ua.random}


def getName(wrapper):
    name = wrapper.find("h1", class_="title").text
    if name:
        return name
    else:
        return "empty_name"


def getPhoto(wrapper, link):
    # получить путь к картинке
    baseURL = link
    photo = wrapper.find("img", class_="img-responsive").get("src")
    absoluteLink = urljoin(baseURL, photo)
    if absoluteLink:
        return absoluteLink
    else:
        return ""


def getBio(wrapper):
    bio = wrapper.find("div", class_="body").text

    if bio:
        return bio
    else:
        return "empty_bio"


def getPersonData(link):
    person = {
        "name": "",
        "photo": "",
        "bio": ""
    }
    response = requests.get(link, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка при запросе: {link},\n статус: {response.status_code}")
        # Возвращаем пустого человека
        return person

    soup = BeautifulSoup(response.text, "lxml")

    for link in links:
        person["photo"] = getPhoto(soup, link)

    person["bio"] = getBio(soup)
    person["name"] = getName(soup)

    return person
