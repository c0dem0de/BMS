# installed modules imported
from os import system as sys

# local files imported
from login import Login


def main_menu():
	while True:
		sys('clear')
		print("    πΉπΈβπ ππΈβπΈπΎπΌππΌβπ πππππΌπ")
		print("\n\
	βββββββββββββββ--ββ\n\
	β     β Login     β\n\
	β     β Exit      β\n\
	βββββββββββββββββ-β")

		choose = input("\nChoose an option[1/2]: ")

		if choose == '1':
			sys('clear')
			print("    πΉπΈβπ ππΈβπΈπΎπΌππΌβπ πππππΌπ")
			print("\n\
	βββββββββββββββ--ββ\n\
	β     β Login     β\n\
	β     β Exit      β\n\
	βββββββββββββββββ-β")
			Login()

		elif choose == '2':
			sys('clear')
			print("    πΉπΈβπ ππΈβπΈπΎπΌππΌβπ πππππΌπ")
			print("\n\
	βββββββββββββββ--ββ\n\
	β     β Login     β\n\
	β     β Exit      β\n\
	βββββββββββββββββ-β")
			print("\n   	     ThankYou")
			input("Press enter to exit")
			sys('clear')
			break

		else:
			print("PLease enter correct choice[1/2]")
			input("Press enter to exit")

main_menu()

# EMPLOYEES:
	# username :John 
	# password : pwd
