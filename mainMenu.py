from os import system as sys
from login import Login 


# main_menue()
def main_menue():
	
	print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
	print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇   ○ Login       ┇\n\
	┇   ○ Exit        ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")

	choose = int(input("\nChoose an option[1/2]: "))

	if choose == 1:
		sys('clear')
		print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
		print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇   ◉ Login       ┇\n\
	┇   ○ Exit        ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")
		Login()

	elif choose == 2:
		sys('clear')
		print("    𝔹𝔸ℕ𝕂 𝕄𝔸ℕ𝔸𝔾𝔼𝕄𝔼ℕ𝕋 𝕊𝕐𝕊𝕋𝔼𝕄")
		print("\n\
	╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑╗\n\
	┇   ○ Login       ┇\n\
	┇   ◉ Exit        ┇\n\
	╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-╝")
		print("\n   	     ThankYou")


main_menue()

# John: admin
# Mark: mark01 
