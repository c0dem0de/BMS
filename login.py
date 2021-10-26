from bullet import Password
from encrypter import encrypter
import mysql.connector

usr = input("Enter usrname: ")
pwd = input("Enter pwd: ")
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()

def Login():
	userName = input("\n\t\t\t\t\t\t\t⇢ user name: ")
	pointr.execute("SELECT * FROM employees")

	for i in pointr:
		if i[1] == userName:
	
			password = Password(prompt='\t\t\t\t\t\t\t⇢ Password: ', hidden='*').launch()
			encrypted_Key = encrypter(password)
			pointr.execute("SELECT * FROM employees")

			for i in pointr:
				if i[2] == encrypted_Key:
					print("\t\t\t\t\t\t\t    Logged In ✔")
					break
				else:
					print("\t\t\t\t\t\t    !!!Incorrect Password!!!")
					break
		else:
			print("\t\t\t\t\t\t    !!!Incorrect Username!!!")
			break


