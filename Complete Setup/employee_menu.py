# installed modules imported
from random import randrange
from os import system as sys


#----------Employee Menu----------
def menu():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Create Account     ┇\n\
	┇   ○ Retrieve Account   ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Account Holders    ┇\n\
	┇   ○ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	inp = input("\nChoose an option[1-6]: ")
	return inp

#----------Create Account Function----------
def create_account():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ◉ Create Account     ┇\n\
	┇   ○ Retrieve Account   ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Account Holders    ┇\n\
	┇   ○ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	
	name = input("Enter Account Holder\'s Name: ")
	acc_type = input("Enter Account Type(C/S): ")
	address = input(f"Enter {name}\'s Address: ")
	ph_no = input(f"Enter {name}\'s Phone_no: ")
	try:
		initial_depo = int(input("Enter the initial deposit amount: "))
	except ValueError:
		print("Enter a valid initial amount")
		input("Press enter to continue ...")
		sys('clear')
		create_account()
	gen_pass =name[0] + name[-1] + str(randrange(112,999))
	
	pointr.execute("SELECT max(ID) FROM members")
	for i in pointr:
		last_id = i
	
	try:
		data = (int(last_id[0])+1, name, gen_pass, acc_type, address, ph_no, initial_depo)
	except TypeError:
		data = (1, name, gen_pass, acc_type, address, ph_no, initial_depo)

	# ID,NAME,PASS,TYPE,ADDRESS,PHONE_NO,BALANCE
	pointr.execute("INSERT INTO members VALUES (%s,%s,%s,%s,%s,%s,%s)",data)
	base.commit()
	sys('clear')
	
	align1 = " " * (20 - len(name))
	align2 = " " * 15
	print(f"\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑---------------╗\n\
	┇   User_id:{name}{align1} ┇\n\
	┇   Password:{gen_pass}{align2}┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑----------------╝")
	input("Press Enter to continue ...")

#----------Get info of selected acc----------
def retrieve_account():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Create Account     ┇\n\
	┇   ◉ Retrieve Account   ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Account Holders    ┇\n\
	┇   ○ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	
	try:
		acc_no = int(input("Enter the account no: "))
	except ValueError:
		print("Enter a valid account no")
		input("Press enter to continue ...")
		sys('clear')
		retrieve_account()
	
	pointr.execute("SELECT * FROM members WHERE ID=%s",(acc_no,))
	data = list(pointr)
	sys('clear')
	
	try:
		print(f"\n\
		╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑╗\n\
		┇   AccountNo: {data[0][0]}          ┇\n\
		┇   AccountName: {data[0][1]}        ┇\n\
		┇   AccountType: {data[0][3]}        ┇\n\
		┇   Address: {data[0][4]}            ┇\n\
		┇   Phoneno: {data[0][5]}            ┇\n\
		┇   Balance: {data[0][6]}            ┇\n\
		╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑╝")
	except IndexError:
		print("The record doesnt exist !!!")
	input("Press Enter to continue ...")

#----------Get transactions of the selected acc----------
def transactions():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Create Account     ┇\n\
	┇   ○ Retrieve Account   ┇\n\
	┇   ◉ Transactions       ┇\n\
	┇   ○ Account Holders    ┇\n\
	┇   ○ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	
	pointr.execute("SELECT * FROM transactions")
	print("ID\tOperation\tAmount\tAccountno")
	
	for i in pointr:
		print(f"{i[0]}\t{i[1]}\t\t{i[2]}\t{i[3]}")
	input("Press enter to continue ...")

#----------Get all acc holders in the bank----------
def account_holder():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Create Account     ┇\n\
	┇   ○ Retrieve Account   ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ◉ Account Holders    ┇\n\
	┇   ○ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	
	pointr.execute("SELECT ID,NAME FROM members")
	print("Accountno\tName")
	
	for i in pointr:
		print(f"{i[0]}\t\t{i[1]}")
	input("Press enter to continue ...")

#----------Remove selected acc----------
def remove_account():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Create Account     ┇\n\
	┇   ○ Retrieve Account   ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Account Holders    ┇\n\
	┇   ◉ Remove Account     ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	
	try:
		acc_no = int(input("Enter the account no: "))
	except ValueError:
		print("Enter a valid account no")
		input("Press enter to continue ...")
		sys('clear')
		remove_account()
	
	pointr.execute("DELETE FROM members WHERE ID=%s",(acc_no,))
	base.commit()


def main(base_arg,pointr_arg):
	global base,pointr
	base = base_arg
	pointr = pointr_arg
	
	while True:
		sys('clear')
		inp = menu()
		sys('clear')
		if inp == '1':
			create_account()
		elif inp == '2':
			retrieve_account()
		elif inp == '3':
			transactions()
		elif inp == '4':
			account_holder()
		elif inp == '5':
			remove_account()
		elif inp == '6':
			break
		else:
			print("Print a valid choice between 1-6")
