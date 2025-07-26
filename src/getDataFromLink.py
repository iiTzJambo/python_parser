import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin
from time import sleep
import tempfile

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

    borderWrapper = wrapper.find("div", class_="border-wrapper")
    img_tag = borderWrapper.find("img", class_="img-responsive")
    photo_url = img_tag.get("src")
    absolute_link = urljoin(link, photo_url)

    response = requests.get(absolute_link, headers=headers)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    return tmp_file_path


def getBio(wrapper):
    borderWrapper = wrapper.find("div", class_="border-wrapper")
    bio = borderWrapper.find("div", class_="body").text

    replaceWords = ["\n", "\r", "\n1", "\n2",
                    "\n3", "\n4", "\n5", "\n6", "\n7", "\n8"]

    for word in replaceWords:
        bio = bio.replace(word, "")
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
        print(
            f"Ошибка при запросе на: {link}, status code = {response.status_code}"
        )
        return person
    else:
        print(f"200 \n {link}")

    soup = BeautifulSoup(response.text, "lxml")
    # print("SOUP: ", soup)

    person["photo"] = getPhoto(soup, link)

    person["name"] = getName(soup)
    person["bio"] = getBio(soup)

    return person
