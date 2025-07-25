from getLinksFromTxt import links
from getDataFromLink import getPersonData
from writePersonInFile import saveInFile

personsList = []

for link in links:
    print(f"Обрабатывается ссылка:{link}")
    person = getPersonData(link)
    saveInFile(person, person["name"])
    print(person)
