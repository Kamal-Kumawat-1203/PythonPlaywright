"""
There are 2 scenarios for adding data in a file.
1. File is located outside the working directory.
2. File is located inside the working directory.
"""

import openpyxl
import os
from Logs.read_Excel_file import workbook

file_path = r"C:\Users\kumaw\Desktop\testdata.xlsx"
# # Uncomment the line below, if Excel file is located in the working directory
# file_path = r"..//excel//testdata.xlsx"

if not os.path.exists(file_path):
    print(f"File not found at {file_path}")
else:
    workbook = openpyxl.load_workbook(file_path)
    # workbook = openpyxl.load_workbook("..//excel//testdata.xlsx")
    if "LoginTests" not in workbook.sheetnames:
        print("Login tests not found")
    else:
        sheet = workbook["LoginTests"]

        # # After adding the column name, comment below 2 lines

        # sheet.cell(row=1, column=4).value="Gender"
        # workbook.save(file_path)

        # # The code below must be enabled after adding the column name
        # # Code below is to input data in rows and columns
        for rows in range(4, 8):
            for cols in range(1, 5):
                sheet.cell(row=rows, column=cols).value="Test12"
        workbook.save(file_path)

"""
After running the code must open excel file becasue here data does not show properly
Or sometimes it shows old data
"""
