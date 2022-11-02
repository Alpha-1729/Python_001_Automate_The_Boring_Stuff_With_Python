#!/usr/bin/python3
# Dealing with pdf

"""
>>>> PyPDF2 doesn't work with some pdf files.
        PyPDF can't extract images from the pdf file.
        You can only get text using this module.

>>>> Download sample pdf file
        https://autbor.com/meetingminutes1.pdf
        https://autbor.com/meetingminutes2.pdf

>>>> pip install PyPDF2
>>>>
>>>>
"""
import PyPDF2
pdf_file = open("sample.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf_file)

# Reading the pages of the pdf file.
print(reader.numPages)

# Getting the text in the page.
page = reader.getPage(0)
page_text = page.extractText()
print(page_text)

# Getting all the text in the pdf file.
for page_num in range(reader.numPages):
    page = reader.getPage(page_num)
    print(page.extractText())

print(" ")
