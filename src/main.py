from getDataFromLink import getPersonData
from writePersonInFile import saveInFile
import time

linkPath = "./links.txt"
links = []

with open(linkPath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        links.append(line.strip())

personsList = []

for link in links[:]:
    person = getPersonData(link)
    time.sleep(1)
    if person["name"]:
        personsList.append(person)


for idx, person in enumerate(personsList):
    print(person['name'])
    saveInFile(person, person['name'])
    time.sleep(2)
