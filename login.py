from bullet import Password
# from encrypter import encrypter
import mysql.connector
from os import system as sys
import employee_menu
# from modulez import *


usr = input("Enter usrname: ")
pwd = Password(prompt='Enter pwd: ', hidden='*').launch()
# usr = "home"
# pwd = "Trio1-Pope-Overbill"
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()
sys('clear')

def Login():
	userName = input("\n\t ⇢ user name: ")

	# EMPLOYEES
	employees = []
	pointr.execute("SELECT * FROM employees")
	for i in pointr:
		employees.append(i[1])
	
	passwords = []
	pointr.execute("SELECT * FROM employees")
	for j in pointr:
		passwords.append(j[2])

	# MEMBERS
	members = []
	pointr.execute("SELECT * FROM members")
	for i in pointr:
		members.append(i[1])
	
	mem_passwords = []
	pointr.execute("SELECT * FROM members")
	for j in pointr:
		mem_passwords.append(j[2])
	

	# check credentials
	if userName in employees:
		password = Password(prompt='\t ⇢ Password: ', hidden='*').launch()
		encrypted_Key = password

		if encrypted_Key in passwords:
			print("\t    Logged In ✔")
			print("\t  Hello Employee")
			input("Press Enter to continue")
			sys('clear')
			employee_menu.main(base,pointr)

		else:
			print("      !!Incorrect Password!!")

	elif userName in members:
		password = Password(prompt='\t ⇢ Password: ', hidden='*').launch()
		encrypted_Key = password

		if encrypted_Key in mem_passwords:
			print("\t    Logged In ✔")
			print("\t  Hello Member")


		else:
			print("      !!Incorrect Password!!")

	else:

		print("      !!Incorrect Username!!")


# Login()
