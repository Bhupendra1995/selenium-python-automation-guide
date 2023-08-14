from openpyxl import Workbook

wb = Workbook()
ws = wb.active

for i in range(1,6):
    for j in range(1,5):
        ws.cell(row=i, column=j).value =i+j
wb.save("first.xlsx")

