def main(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}')
	pointr = base.cursor()
	pointr.execute("SHOW DATABASES")
	data = list(pointr)
	dbs = []
	for i in data:
		dbs.append(i[0])
	if "bms" not in dbs:
		create_DB(usr,pwd)
	else:
		base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
		pointr = base.cursor()
		pointr.execute("SHOW TABLES")
		tbls = []
		data = list(pointr)
		for i in data:
			tbls.append(i[0])
		if 'employees' not in tbls:
			create_employees(usr,pwd)
		if 'members' not in tbls:
			create_members(usr,pwd)
		if 'transactions' not in tbls:
			create_transaction(usr,pwd)
	base.commit()
	del pointr
	del base
	

def create_DB(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}')
	pointr = base.cursor()
	pointr.execute('CREATE DATABASE bms')
	create_employees(usr,pwd)
	create_members(usr,pwd)
	create_transaction(usr,pwd)

def create_employees(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
	pointr = base.cursor()
	pointr.execute("create table employees(emp_ID INT PRIMARY KEY,emp_NAME VARCHAR(30),emp_KEY VARCHAR(500))")

def create_members(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
	pointr = base.cursor()
	pointr.execute("create table members(ID INT PRIMARY KEY,NAME VARCHAR(30),PASS VARCHAR(100),TYPE VARCHAR(30),ADDRESS VARCHAR(300),PHONE_NO VARCHAR(15),BALANCE INTEGER)")

def create_transaction(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
	pointr = base.cursor()
	pointr.execute("create table transactions(ID INT PRIMARY KEY,OPERATION VARCHAR(40),AMOUNT INT,ACCOUNT_NO INT NOT NULL)")	