#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# from os import system as sys
# from time import sleep as slp

# def login():
# 	usr_id = input("\n							⇢ User Id: ")
# 	usr_id = input("							⇢ Password: ")

# def main_menue():

# 	print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
# 	print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
# 	print("\t\t\t\t\t\t┇\t   ○ Login\t     ┇")
# 	print("\t\t\t\t\t\t┇\t   ○ Exit\t     ┇")
# 	print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")

# 	choose = int(input("\n						Choose an option[1/2]: "))

# 	if choose == 1:
# 		sys('clear')
# 		print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
# 		print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
# 		print("\t\t\t\t\t\t┇\t   ◉ Login\t     ┇")
# 		print("\t\t\t\t\t\t┇\t   ○ Exit\t     ┇")
# 		print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")
# 		login()

# 	elif choose == 2:
# 		sys('clear')
# 		print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
# 		print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
# 		print("\t\t\t\t\t\t┇\t   ○ Login\t     ┇")
# 		print("\t\t\t\t\t\t┇\t   ◉ Exit\t     ┇")
# 		print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")

# main_menue()

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# import mysql.connector
# from bullet import Password

# pwd = Password(prompt='Enter Password: ', hidden='*')
# pwd=pwd.launch()
# base = mysql.connector.connect(host='localhost', user='home', passwd=f'{pwd}', database='tester')
# cursor= base.cursor()
  
# # execute your query
# cursor.execute("SELECT * FROM Persons")
  
# # fetch all the matching rows 
# result = cursor.fetchall()
  
# # loop through the rows
# for row in result:
#     print(row)
#     print("\n")
# # print("Connection Successfull!!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# # from time import sleep as slp
# # print("He\bl\bl\bo\b ", end="")
# # slp(1)
# # print("\rHel\bl\bo\b ", end="")
# # slp(1)
# # print("\rHell\bo\b ", end="")
# # slp(1)
# # print("\rHello\b ", end="")
# # slp(1)
# # print("\rHello", end="")
# # for i in range(10):
# # 	print('\r₹', end="")
# # 	slp(0.2)
# # 	print('\r＄', end="")
# # 	slp(0.2)
# # 	print('\r￥', end="")
# # 	slp(0.2)
# # 	print('\r￡', end="")

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# # import sys, time, threading
# # def the_process_function():
# #     n = 20
# #     for i in range(n):
# #         time.sleep(1)
# #         sys.stdout.write('\r'+'loading...  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
# #         sys.stdout.flush()
# #     sys.stdout.write('\r'+'loading... finished               \n')
# # the_process_function()
# # def animated_loading():
# #     chars = "/—\\|" 
# #     for j in range(10):
# # 	    for char in chars:	
# # 	        sys.stdout.write('\r'+'loading...'+char)
# # 	        time.sleep(.1)
# # 	        sys.stdout.flush() 
# # animated_loading()

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

import mysql.connector
from bullet import Password

def Login():
	userName = input("Enter user name: ")
	password = Password(prompt='Enter Password: ', hidden='*').launch()

	connection = mysql.connector.connect(host='localhost', user=f'{userName}', passwd=f'{password}')
	
	cursor = connection.cursor()

	databases = []

	cursor.execute("SHOW DATABASES")

	for x in cursor:
	  databases.append(x[0])

	# print(databases)

	if 'bms' in databases:
		print("Connection Availabale!!")
	else:
		print("!!Connection need to be created!!")

Login()
