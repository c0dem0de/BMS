# installed modules imported
from os import system as sys

# local files imported
from login import Login


def main_menu():
	while True:
		sys('clear')
		print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
		print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇     ○ Login     ┇\n\
	┇     ○ Exit      ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")

		choose = input("\nChoose an option[1/2]: ")

		if choose == '1':
			sys('clear')
			print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
			print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇     ◉ Login     ┇\n\
	┇     ○ Exit      ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")
			Login()

		elif choose == '2':
			sys('clear')
			print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
			print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇     ○ Login     ┇\n\
	┇     ◉ Exit      ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")
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
