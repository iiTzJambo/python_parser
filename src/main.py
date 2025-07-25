from getLinksFromTxt import links
from getDataFromLink import getPersonData
from writePersonInFile import saveInFile

personsList = []

for link in links:
    person = getPersonData(link)

    if person["name"]:
        personsList.append(person)

print(personsList)

for person in personsList:
    saveInFile(person, person["name"])
