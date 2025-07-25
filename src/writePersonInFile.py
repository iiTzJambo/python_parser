from docx import Document
# from getDataFromLink import getPersonData

templatePath = "./template.docx"
personsPath = "persons/"

doc = Document(templatePath)


def saveInFile(person, fileName):
    doc.paragraphs[1].text = person["name"]
    doc.paragraphs[2].text = person["photo"]
    # doc.paragraphs[4].text = person.org_name
    # doc.paragraphs[6].text = person.job
    # doc.paragraphs[8].text = person.job
    # doc.paragraphs[10].text = person.rank
    # doc.paragraphs[12].text = person.exp
    # doc.paragraphs[14].text = person.educ
    doc.paragraphs[16].text = person["bio"]
    # doc.paragraphs[18].text = person.source
    # doc.paragraphs[20].text = person.create
    doc.save(f"{personsPath}{fileName}.docx")
