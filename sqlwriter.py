import mysql.connector

usr = "home"
pwd = "Trio1-Pope-Overbill"
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()

# Insert data to DB
def DATA_INSERT():
	ID = int(input("Enter ID: "))
	NAME = input("Enter NAME: ")
	PWD = input("Enter PWD: ")
	sql = "INSERT INTO employees (emp_ID, emp_NAME, emp_KEY) VALUES (%s, %s, %s)"
	val = (ID, f"{NAME}", f"{PWD}")	
	pointr.execute(sql, val)
	base.commit()

# Delete data form DB
def DATA_DELETE():
	pointr.execute("DELETE FROM employees WHERE emp_NAME='Mark'")
	base.commit()

# Extract DB 
def DATA_EXTRACT():
	pointr.execute("SELECT * FROM employees")
	for i in pointr:
		print(i)


# DATA_INSERT()
# DATA_DELETE()
DATA_EXTRACT()
