from docx import Document
from docx.shared import Inches

personsPath = "persons/"


def saveInFile(person, fileName):
    doc = Document()
    photo = ''

    print(person, '1123')

    doc.add_heading(person["name"], 1)

    if person["photo"] == '':
        photo = 'C:\Program Files\GitHub\python_parser\IMAGE.png'
    else:
        photo = person["photo"]

    doc.add_picture(photo, width=Inches(3), height=Inches(3.25))

    doc.add_paragraph(person["personalInfo"])

    doc.save(f"{personsPath}/{fileName}.docx")
