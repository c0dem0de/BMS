import mysql.connector
from animations import *
from bullet import Password
from os import system as sys
from time import sleep

def BMS_Connect():
	userName = input("\n\t ⇢ user name: ")
	password = Password(prompt='\n\t ⇢ Password: ', hidden='*').launch()

	try:
		connection = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}')
		sys('clear')
		connect_Anim_SERVER()
		print("\rConnected to server         ")
		main_cursor = connection.cursor()

		databases = []

		main_cursor.execute("SHOW DATABASES")

		for x in main_cursor:
		  databases.append(x[0])


		if 'bms' in databases:
			sleep(0.5)
			print("DB found!!")
			connect_Anim_DB()
			bms_connect = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}', database='bms') 
			sleep(0.5)
			sys('clear')
			print("Connected to DB!!")
		
		else:
			sleep(0.5)
			print("DB NOT found!!")
			sleep(1)
			main_cursor.execute("CREATE DATABASE bms")
			create_DB()
			sleep(1)
			print("Database Created!!")
			bms_connect = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}', database='bms')	

			






	except mysql.connector.Error as err:
		print("Something went wrong: ''{}''".format(err))


	

BMS_Connect()
