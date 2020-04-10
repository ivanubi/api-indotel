import xlrd
import pymysql

book = xlrd.open_workbook("excel_numbers.xlsx")
sheet = book.sheet_by_name("nxxkist")

database = pymysql.connect (
host="localhost",
user = "username",
passwd = "password",
db = "indotel")

cursor = database.cursor()
query = """INSERT INTO indotel (prestadora, tipo, npa, nxx) VALUES (%s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
	prestadora	= sheet.cell(r,0).value
	tipo        = sheet.cell(r,1).value
	npa			= sheet.cell(r,2).value
	nxx		    = sheet.cell(r,3).value
	values = (prestadora, tipo, npa, nxx)
	cursor.execute(query, values)
	
cursor.close()
database.commit()
database.close()
print("")
print("DONE!")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("You just imported " + columns + " columns and " + rows + " rows to MySQL!")
