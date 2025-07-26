import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from getLinksFromTxt import links
from urllib.parse import urljoin
from time import sleep

ua = UserAgent()
headers = {"User-Agent": ua.random}


def getName(wrapper):
    borderWrapper = wrapper.find("div", class_="border-wrapper")
    name = wrapper.find("h1", class_="title").text
    if name:
        return name
    else:
        return "empty_name"


def getPhoto(wrapper, link):
    # получить путь к картинке
    baseLink = link
    borderWrapper = wrapper.find("div", class_="border-wrapper")
    photo = borderWrapper.find("img", class_="img-responsive").get("src")
    absoluteLink = urljoin(baseLink, photo)
    if absoluteLink:
        return absoluteLink
    else:
        return ""


def getBio(wrapper):
    borderWrapper = wrapper.find("div", class_="border-wrapper")
    bio = borderWrapper.find("div", class_="body").text
    if bio:
        return bio
    else:
        return "empty_bio"


def getPersonData(link):
    sleep(10)
    person = {
        "name": "",
        "photo": "",
        "bio": ""
    }
    response = requests.get(link, headers=headers)

    if response.status_code != 200:
        # сделать вывод ошибок красивым
        print(
            f"Ошибка при запросе на: {link}, status code = {response.status_code}"
        )
        return person
    else:
        print(f"200 \n {link}")

    soup = BeautifulSoup(response.text, "lxml")
    # print("SOUP: ", soup)

    for link in links:
        person["photo"] = getPhoto(soup, link)

    person["name"] = getName(soup)
    person["bio"] = getBio(soup)

    return person
