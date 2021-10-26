from time import sleep as slp

def connect_Anim():
	for i in range(3):
		print("\r                                     ", end="")
		slp(0.0)
		print('\rConnecting to SQL Account.', end="")
		slp(0.3)
		print('\rConnecting to SQL Account..', end="")
		slp(0.3)
		print('\rConnecting to SQL Account...', end="")
		slp(0.3)
