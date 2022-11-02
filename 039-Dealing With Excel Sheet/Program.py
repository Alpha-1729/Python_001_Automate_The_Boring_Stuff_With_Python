#!/usr/bin/python3
# Dealing with excel sheet

"""
>>>> pip install openpyxl
>>>> If a cell contain a date value.
        The output will be in a datetime object format.
        Convert the cell value to string to get the exact value in the cell.
>>>>
>>>>
>>>>
"""
import openpyxl
workbook = openpyxl.load_workbook("sample.xlsx")

# Getting all the sheet name.
print(workbook.get_sheet_names())

sheet = workbook.get_sheet_by_name("Sheet1")

# Getting the value in a cell.
cell = sheet["G2"]  # Getting the cell value in Gth column and 2 row
print(cell.value)

# Alternate method to get value in the cell.
print(sheet.cell(row=1, column=2).value)  # row and column start at index 1.

print(" ")
