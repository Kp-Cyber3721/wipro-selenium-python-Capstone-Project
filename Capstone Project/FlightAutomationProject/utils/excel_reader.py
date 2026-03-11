import openpyxl
from datetime import datetime
def get_test_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    headers = []
    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        if i == 0:
            headers = row
        else:
            if all(cell is None for cell in row):
                continue
            row_data = []
            for header, cell in zip(headers, row):
                if isinstance(cell, datetime):
                    if header == "dob_month":
                        cell = cell.strftime("%B")
                if cell is None:
                    cell = ""
                row_data.append(cell)
            data.append(dict(zip(headers, row_data)))
    return data