from os import system as sys

def menu():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Account Details    ┇\n\
	┇   ○ Deposit            ┇\n\
	┇   ○ Withdraw           ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	inp = input("\nChoose an option[1-5]: ")
	return inp

def account_details():
	pointr.execute("SELECT * FROM members WHERE ID=%s",(mem_id,))
	data = list(pointr)
	print(f"\n\
		╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑╗\n\
		┇   AccountNo: {data[0][0]}          ┇\n\
		┇   AccountName: {data[0][1]}        ┇\n\
		┇   AccountType: {data[0][3]}        ┇\n\
		┇   Address: {data[0][4]}            ┇\n\
		┇   Phoneno: {data[0][5]}            ┇\n\
		┇   Balance: {data[0][6]}            ┇\n\
		╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑╝")
	input("Press Enter to continue ...")

def deposit():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Account Details    ┇\n\
	┇   ◉ Deposit            ┇\n\
	┇   ○ Withdraw           ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	try:
		dep = int(input("Enter the amount:"))
	except ValueError:
		print("Enter a valid amount")
		input("Press enter to continue...")
		sys('clear')
		deposit()
	inp = input("Are you sure(y/n): ")
	if inp.lower() == 'y':
		pointr.execute("SELECT BALANCE FROM members WHERE ID=%s",(mem_id,))
		data = list(pointr)
		pointr.execute("SELECT max(ID) FROM transactions")
		for i in pointr:
			last_id = i
		try:	
			pointr.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",(int(last_id[0])+1,"D",dep,mem_id))
		except TypeError:
			pointr.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",(1,"D",dep,mem_id))
		dep += int(data[0][0])
		pointr.execute("UPDATE members SET BALANCE = %s WHERE ID=%s",(dep,mem_id))
		base.commit()
	elif inp.lower() == 'n':
		pass
	else:
		print("Enter a valid choice(y/n)")
		input("Press enter to continue ...")
		sys('clear')
		deposit()


def withdraw():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Account Details    ┇\n\
	┇   ○ Deposit            ┇\n\
	┇   ◉ Withdraw           ┇\n\
	┇   ○ Transactions       ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	try:
		wit = int(input("Enter the amount:"))
	except ValueError:
		print("Enter a valid amount")
		input("Press enter to continue...")
		sys('clear')
		withdraw()
	inp = input("Are you sure(y/n): ")
	if inp == 'y' or inp == "Y":
		pointr.execute("SELECT BALANCE FROM members WHERE ID=%s",(mem_id,))
		data = list(pointr)
		if (int(data[0][0]) - wit) >= 0:
			pointr.execute("SELECT max(ID) FROM transactions")
			for i in pointr:
				last_id = i
			try:
				pointr.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",(int(last_id[0])+1,"W",wit,mem_id))
			except TypeError:
				pointr.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",(1,"D",dep,mem_id))
			wit = int(data[0][0]) - wit
			pointr.execute("UPDATE members SET BALANCE = %s WHERE ID=%s",(wit,mem_id))
			base.commit()
		else:
			print("Insuffiecient balance")
			input("Press enter to continue ...")
			sys('clear')
			withdraw()
	elif inp == 'n' or 'N':
		pass
	else:
		print("Enter a valid choice(y/n)")
		input("Press enter to continue ...")
		sys('clear')
		withdraw()

def transactions():
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
	┇   ○ Account Details    ┇\n\
	┇   ○ Deposit            ┇\n\
	┇   ○ Withdraw           ┇\n\
	┇   ◉ Transactions       ┇\n\
	┇   ○ Log Out            ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
	pointr.execute("SELECT * FROM transactions WHERE ACCOUNT_NO=%s",(mem_id,))
	print("Operation\tAmount")
	for i in pointr:
		print(f"{i[1]}\t\t{i[2]}")
	input("Press enter to continue ...")

def main(base_arg,pointr_arg,mem_name):
	global base,pointr,mem_id
	base = base_arg
	pointr = pointr_arg
	pointr.execute("SELECT ID FROM members WHERE NAME=%s",(mem_name,))
	data = list(pointr)
	mem_id = data[0][0]
	del data
	while True:
		sys('clear')
		inp = menu()
		sys('clear')
		if inp == '1':
			account_details()
		elif inp == '2':
			deposit()
		elif inp == '3':
			withdraw()
		elif inp == '4':
			transactions()
		elif inp == '5':
			break
		else:
			print("Print a valid choice between 1-6")
