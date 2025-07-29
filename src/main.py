from getDataFromLink import getPersonData
from writePersonInFile import saveInFile

linkPath = "./links.txt"
links = []

with open(linkPath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        links.append(line)
    # print(links)

personsList = []

for link in links[:]:
    person = getPersonData(link)

if person["name"]:
    personsList.append(person)

print(personsList)

for person in personsList:
    saveInFile(person, person["name"])
