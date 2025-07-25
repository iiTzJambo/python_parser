import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random}


def getName(wrapper):
    name = wrapper.find("h1", class_="title").text
    if name:
        return name
    else:
        return "empty_name"


def getPhoto(wrapper):
    # получить путь к картинке
    photo = wrapper.find("img", class_="img-responsive").get("src")

    if photo:
        return photo
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
        # сделать вывод ошибок красивым
        print(
            f"Ошибка при запросе на: {link}, status code = {response.status_code}"
        )
        return person

    soup = BeautifulSoup(response.text, "lxml")
    # print("SOUP: ", soup)

    person["name"] = getName(soup)
    person["photo"] = getPhoto(soup)
    person["bio"] = getBio(soup)

    return person
