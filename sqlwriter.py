import mysql.connector

usr = "home"
pwd = "Trio1-Pope-Overbill"
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()


# pointr.execute("INSERT INTO employees VALUES (102, 'Mark', 'ejfieififbfiejeifieifiejfafifafiejfffifdfifdfafifcfifeej')")
# pointr.execute("DELETE FROM employees WHERE emp_NAME='Mark'")
# base.commit()

# Extract DB 
pointr.execute("SELECT * FROM employees")
for i in pointr:
	print(i)
