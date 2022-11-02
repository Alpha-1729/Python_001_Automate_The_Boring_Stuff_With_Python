#!/usr/bin/python3
# Dealing with pdf 2

"""
>>>> PyPDF2 can done page level editing such as
    merging pdf and removing the pages from the pdf file.
>>>>
>>>>
>>>>
>>>>
"""
import PyPDF2

pdf1 = open("sample1.pdf", "rb")
pdf2 = open("sample2.pdf", "rb")

reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)

# Creating a writer object
writer = PyPDF2.PdfFileWriter()

# Reading all pages in the pdf1
for page_num in range(reader1.numPages):
    page = reader1.getPage(page_num)
    writer.addPage(page)

# Reading all pages in the pdf2
for page_num in range(reader2.numPages):
    page = reader2.getPage(page_num)
    writer.addPage(page)

# Creating a output file object.
output_file = open("Combined.pdf", "wb")
writer.write(output_file)

output_file.close()
pdf1.close()
pdf2.close()

print(" ")
