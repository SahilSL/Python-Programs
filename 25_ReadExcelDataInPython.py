# Not proper
import xlrd
loc =("E:\\Coding\\Python\\Guvi\\Book1.xlsx")

wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#print(sheet.cell_value(3,3))
print(sheet.ncols)
print(sheet.nrows)