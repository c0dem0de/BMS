from bullet import Password
from encrypter import encrypter
import mysql.connector
from os import system as sys

# usr = input("Enter usrname: ")
# pwd = input("Enter pwd: ")
usr = ""
pwd = ""
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()
sys('clear')

def Login():
	userName = input("\n⇢ user name: ")
	customers = []
	pointr.execute("SELECT * FROM employees")
	for i in pointr:
		customers.append(i[1])

	passwords = []
	pointr.execute("SELECT * FROM employees")
	for j in pointr:
		passwords.append(j[2])
	if userName in customers:
		password = Password(prompt='⇢ Password: ', hidden='*').launch()
		encrypted_Key = encrypter(password)
		# pointr.execute("SELECT * FROM employees")

		if encrypted_Key in passwords:
			print("   Logged In ✔")
			# break
		else:
			print("!!!Incorrect Password!!!")
			# break
	else:
		print("!!!Incorrect Username!!!")
		# break


# Login()
