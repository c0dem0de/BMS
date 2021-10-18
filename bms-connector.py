import mysql.connector
from animations import connect_Anim 
from bullet import Password
from os import system as sys

def BMS_Connect():
	userName = input("\n\t\t\t\t\t\t\t⇢ user name: ")
	password = Password(prompt='\t\t\t\t\t\t\t⇢ Password: ', hidden='*').launch()

	try:
		connection = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}')
		connect_Anim()
		print("Connection Successfull!!")
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

	except mysql.connector.Error as err:
		print("Something went wrong: ''{}''".format(err))


	

BMS_Connect()
