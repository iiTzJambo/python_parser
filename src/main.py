import asyncio
import aiofiles
from getDataFromLink import getPersonData
from writePersonInFile import saveInFile


async def main():
    linkPath = "./links.txt"
    links = []

    async with aiofiles.open(linkPath, 'r', encoding='utf-8') as file:
        lines = await file.readlines()

        for line in lines:
            links.append(line.strip())

    personsList = []

    for link in links[:]:
        person = await getPersonData(link)
        if person["name"]:
            personsList.append(person)

    for idx, person in enumerate(personsList):
        print(person['name'])
        saveInFile(person, person['name'])
asyncio.run(main())
