from time import sleep as slp

def connect_Anim_SERVER():
	for i in range(3):
		print("\r                                     ", end="")
		slp(0.0)
		print('\rConnecting to SQL Server.', end="")
		slp(0.3)
		print('\rConnecting to SQL Server..', end="")
		slp(0.3)
		print('\rConnecting to SQL Server...', end="")
		slp(0.3)

def connect_Anim_DB():
	for i in range(3):
		print("\r                                     ", end="")
		slp(0.0)
		print('\rConnecting to DataBase.', end="")
		slp(0.3)
		print('\rConnecting to DataBase..', end="")
		slp(0.3)
		print('\rConnecting to DataBase...', end="")
		slp(0.3)

def create_DB():
	for i in range(3):
		print("\r                                     ", end="")
		slp(0.0)
		print('\rCreating DataBase.', end="")
		slp(0.3)
		print('\rCreating DataBase..', end="")
		slp(0.3)
		print('\rCreating DataBase...', end="")
		slp(0.3)
