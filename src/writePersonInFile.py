from docx import Document
from docx.shared import Pt, RGBColor, Inches

personsPath = "persons/"

doc = Document()


def saveInFile(person, fileName):

    doc.add_heading(person["name"], 1)

    doc.add_picture(person["photo"], width=Inches(3), height=Inches(3.25))

    paragraph = doc.add_paragraph(person["bio"])

    doc.save(f"{personsPath}{fileName}.docx")
