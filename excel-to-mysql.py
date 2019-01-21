import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("indotel-nxx.xlsx")
sheet = book.sheet_by_name("nxxkist")
# sheet = book.shet_by_index(1)

# Establish a MySQL connection
database = pymysql.connect (
host="localhost",
user = "username",
passwd = "password",
db = "indotel")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO indotel (prestadora, tipo, npa, nxx) VALUES (%s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		prestadora	= sheet.cell(r,0).value
		tipo        = sheet.cell(r,1).value
		npa			= sheet.cell(r,2).value
		nxx		    = sheet.cell(r,3).value

		# Assign values from each row
		values = (prestadora, tipo, npa, nxx)

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("I just imported " + columns + " columns and " + rows + " rows to MySQL!")
