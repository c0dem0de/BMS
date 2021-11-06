# installed modules imported
from os import system as sys
from bullet import Password
import mysql.connector

# local files imported
import employee_menu
import members_menu
import DB_check

usr = input("Enter usrname: ")
pwd = Password(prompt='Enter pwd: ', hidden='*').launch()
DB_check.main(usr, pwd)
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()
sys('clear')

#----------Login to member/employee acc----------
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
	

	# PWD VALIDITY CHECK
	if userName in employees:
		password = Password(prompt='\t ⇢ Password: ', hidden='*').launch()

		if password in passwords:
			print("\t    Logged In ✔")
			print("\t  Hello Employee")
			input("\nPress Enter to continue")
			sys('clear')
			employee_menu.main(base,pointr)

		else:
			print("      !!Incorrect Password!!")
			input("Press enter to continue ...")

	elif userName in members:
		password = Password(prompt='\t ⇢ Password: ', hidden='*').launch()

		if password in mem_passwords:
			print("\t    Logged In ✔")
			print("\t  Hello Member")
			input("\nPress Enter to continue")
			sys('clear')
			members_menu.main(base,pointr,userName)


		else:
			print("      !!Incorrect Password!!")
			input("Press enter to continue ...")

	else:

		print("      !!Incorrect Username!!")
		input("Press enter to continue ...")

