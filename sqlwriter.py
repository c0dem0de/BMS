# from modulez import *
import mysql.connector
from encrypter import encrypter

usr = ""
pwd = ""
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()

# Create Table
def DEF_TABLE():
	pointr.execute("create table members(\
					mem_ID INT PRIMARY KEY,\
					mem_NAME VARCHAR(30),\
					mem_KEY VARCHAR(500)\
					)")
# DEF_TABLE()

# Insert data to DB
def DATA_INSERT():
	print("1. Employees\n2. Members\n")
	table = int(input("Which table: "))
	ID = int(input("Enter ID: "))
	NAME = input("Enter NAME: ")
	PWD = input("Enter PWD: ")
	PWD = encrypter(PWD)
	if table == 1:
		sql = "INSERT INTO employees (emp_ID, emp_NAME, emp_KEY) VALUES (%s, %s, %s)"
		val = (ID, f"{NAME}", f"{PWD}")	
		pointr.execute(sql, val)
	elif table == 2:
		sql = "INSERT INTO members (mem_ID, mem_NAME, mem_KEY) VALUES (%s, %s, %s)"
		val = (ID, f"{NAME}", f"{PWD}")	
		pointr.execute(sql, val)
	base.commit()

# Delete data form DB
def DATA_DELETE():
	print("1. Employees\n2. Members\n")
	table = int(input("Which table: "))
	NAME = input("Enter NAME: ")
	if table == 1:
		pointr.execute(f"DELETE FROM employees WHERE emp_NAME='{NAME}'")
	elif table == 2:
		pointr.execute(f"DELETE FROM members WHERE mem_NAME='{NAME}'")
	base.commit()

# Extract DB 
def DATA_EXTRACT():
	print("1. Employees\n2. Members\n")
	table = int(input("Which table: "))
	if table == 1:
		pointr.execute("SELECT * FROM employees")
		for i in pointr:
			print(i)
	elif table == 2:
		pointr.execute("SELECT * FROM members")
		for i in pointr:
			print(i)


print("1. Insert Data\n2. Delete data\n3. Extract data\n")
opts = int(input("Select: "))

if opts == 1:
	DATA_INSERT()
elif opts == 2:
	DATA_DELETE()
elif opts == 3:
	DATA_EXTRACT()

