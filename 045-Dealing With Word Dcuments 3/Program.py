#!/usr/bin/python3
# Dealing with word dcuments 3

"""
>>>> Here we are creating a python program to get all the text in docx file.
>>>>
>>>>
>>>>
>>>>
"""
import docx

def get_text(file_name):
    full_text = []
    doc = docx.Document(file_name)
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

print(get_text("sample.docx"))
print(" ")
