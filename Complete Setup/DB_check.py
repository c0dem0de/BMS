# installed modules imported
import mysql.connector

#----------Checking for DB existance----------

def main(usr,pwd):
	
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}')
	pointr = base.cursor()
	pointr.execute("SHOW DATABASES")

	dbs = []
	for i in pointr:
		dbs.append(i[0])
	
	if "bms" not in dbs:
		create_DB(usr,pwd)
	else:
		base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
		pointr = base.cursor()
		pointr.execute("SHOW TABLES")
		
		tabls = []
		for i in pointr:
			tabls.append(i[0])
		
		if 'employees' not in tabls:
			create_tables(usr, pwd, '1')
		if 'members' not in tabls:
			create_tables(usr, pwd, '2')
		if 'transactions' not in tabls:
			create_tables(usr, pwd, '3')
	
	base.commit()
	del pointr
	del base
	

#----------Functions to build the DB----------

def create_DB(usr,pwd):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}')
	pointr = base.cursor()
	pointr.execute('CREATE DATABASE bms')
	create_tables(usr, pwd)

def create_tables(usr, pwd, table=''):
	base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
	pointr = base.cursor()

	if '1' in table:
		pointr.execute("create table employees(emp_ID INT PRIMARY KEY,emp_NAME VARCHAR(30),emp_KEY VARCHAR(500))")
		pointr.execute("INSERT INTO employees VALUES(1, 'John', 'pwd')")
	elif '2' in table:
		pointr.execute("create table members(ID INT PRIMARY KEY,NAME VARCHAR(30),PASS VARCHAR(100),TYPE VARCHAR(30),ADDRESS VARCHAR(300),PHONE_NO VARCHAR(15),BALANCE INTEGER)")
	elif '3' in table:
		pointr.execute("create table transactions(ID INT PRIMARY KEY,OPERATION VARCHAR(40),AMOUNT INT,ACCOUNT_NO INT NOT NULL)")
	else:
		pointr.execute("create table employees(emp_ID INT PRIMARY KEY,emp_NAME VARCHAR(30),emp_KEY VARCHAR(500))")
		pointr.execute("INSERT INTO employees VALUES(1, 'John', 'pwd')")
		pointr.execute("create table members(ID INT PRIMARY KEY,NAME VARCHAR(30),PASS VARCHAR(100),TYPE VARCHAR(30),ADDRESS VARCHAR(300),PHONE_NO VARCHAR(15),BALANCE INTEGER)")
		pointr.execute("create table transactions(ID INT PRIMARY KEY,OPERATION VARCHAR(40),AMOUNT INT,ACCOUNT_NO INT NOT NULL)")
