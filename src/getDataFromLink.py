import aiohttp
import asyncio
import aiofiles
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin
import tempfile
import traceback

ua = UserAgent()
headers = {"User-Agent": ua.random}
punct = ['!', '@', '#', '$', '%', '^', '&', '?', '"', '<', '>']


async def getName(wrapper):
    try:
        name = wrapper.find("h1", class_="title").text
        for p in punct:
            name = name.replace(p, '')
        return name
    except AttributeError:
        return name
    except Exception as e:
        print(f"Ошибка при получении имени: {str(e)}")
        return name


async def getPhoto(wrapper, link):
    try:
        borderWrapper = wrapper.find("div", class_="border-wrapper")
        img_tag = borderWrapper.find("img", class_="img-responsive")
        photo_url = img_tag.get("src")
        absolute_link = urljoin(link, photo_url)

        response = requests.get(absolute_link, headers=headers, timeout=10)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(response.content)
            tmp_file_path = tmp_file.name

        return tmp_file_path
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке фото: {str(e)}")
        return ""
    except Exception as e:
        print(f"Неожиданная ошибка при получении фото: {str(e)}")
        return ""


async def getPersonalInfo(wrapper):
    try:
        borderWrapper = wrapper.find("div", class_="border-wrapper")
        body = borderWrapper.find("div", class_="body").text
        replaceWords = ["\n", "\r", "\n1", "\n2",
                        "\n3", "\n4", "\n5", "\n6", "\n7", "\n8"]

        for word in replaceWords:
            body = body.replace(word, "")
        return body if body else "empty_bio"
    except AttributeError:
        return "empty_bio"
    except Exception as e:
        print(f"Ошибка при получении информации: {str(e)}")
        return "empty_bio"


async def response(link):
    response = requests.get(link, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    return soup


async def getPersonData(link):
    person = {
        "name": "Person",
        "photo": "IMAGE.png",
        "personalInfo": ""
    }

    try:
        soup = await response(link)

        person["photo"] = await getPhoto(soup, link)
        person["name"] = await getName(soup)
        person["personalInfo"] = await getPersonalInfo(soup)

    except requests.exceptions.Timeout:
        print(f"Превышено время ожидания сервера для ссылки {link}")
    except requests.exceptions.ConnectionError:
        print(f"Не удалось подключиться к серверу для ссылки {link}")
    except requests.exceptions.HTTPError as err:
        print(
            f"Ошибка при запросе для ссылки {link}: {err.response.status_code}")
    except Exception as e:
        print(f"Неожиданная ошибка при обработке ссылки {link}: {str(e)}")
        traceback.print_exc()

    return person
