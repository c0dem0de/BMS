from os import system as sys
from time import sleep as slp
from login import Login

def main_menue():

	print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
	print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
	print("\t\t\t\t\t\t┇\t   ○ Login\t     ┇")
	print("\t\t\t\t\t\t┇\t   ○ Exit\t     ┇")
	print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")

	choose = int(input("\n						Choose an option[1/2]: "))

	if choose == 1:
		sys('clear')
		print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
		print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
		print("\t\t\t\t\t\t┇\t   ◉ Login\t     ┇")
		print("\t\t\t\t\t\t┇\t   ○ Exit\t     ┇")
		print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")
		Login()

	elif choose == 2:
		sys('clear')
		print("\t\t\t\t\t\t𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
		print("\t\t\t\t\t        ╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╗")
		print("\t\t\t\t\t\t┇\t   ○ Login\t     ┇")
		print("\t\t\t\t\t\t┇\t   ◉ Exit\t     ┇")
		print("\t\t\t\t\t        ╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‐‑‑‑‑‑‑‑‑╝")

main_menue()
