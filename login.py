import mysql.connector
from bullet import Password

def Login():
	userName = input("Enter user name: ")
	password = Password(prompt='Enter Password: ', hidden='*').launch()

	connection = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}')
	
	main_cursor = connection.cursor()

	databases = []

	main_cursor.execute("SHOW DATABASES")

	for x in main_cursor:
	  databases.append(x[0])


	if 'bms' in databases:
		bms_connect = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}', database='bms') 
		print("Connection Made!!")
	
	else:
		main_cursor.execute("CREATE DATABASE bms")
		print("Database Created!!")
		bms_connect = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}', database='bms')
		print("Connection Made!!")	

Login()
