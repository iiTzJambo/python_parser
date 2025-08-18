from docx import Document
from docx.shared import Inches
import time


personsPath = "persons/"


def saveInFile(person, fileName):
    if (person["name"] is None):
        return

    doc = Document()

    print(f'Person name: {person['name']} ')

    doc.add_heading(person["name"], 1)

    doc.add_picture(person['photo'], width=Inches(3), height=Inches(3.25))

    doc.add_paragraph(person["personalInfo"])

    doc.save(f"{personsPath}/{fileName}.docx")
