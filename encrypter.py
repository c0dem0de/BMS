chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
		 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
		 '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
		 '+', '-', '*', '/', '%', '!', '@', '#', '$', '^',
		 '&', '*', '(', ')', '_', '=', '{', '}', '[', ']',
		 '<', ',', '>', '.', '?', '/', '"', "'", '|', '\\',
		 ';', ':', '~', '`'] 

def encrypter(pwd):
	# pwd = input('Enter your pwd: ')
	key = []
	key_sort = []
	indexes = {}
	indexes_sorted = {}

	encrypted = ""

	for i in pwd:
		key.append(chars.index(i))
		key_sort.append(chars.index(i))

	for i in range(len(pwd)):
		indexes[i] = key[i]

	def indexes_sorts():
		for i in sorted(indexes.values()):
		    for k in indexes.keys():
		        if indexes[k] == i:
		            indexes_sorted[k] = indexes[k]
		            break

	key_sort.sort()
	indexes_sorts()
	ind_keys = list(indexes_sorted.keys())
	ind_vals = list(indexes_sorted.values())
	for i in range(len(indexes_sorted)):
		encrypted += f"{ind_keys[i]}:{ind_vals[i]}:"

	# print(encrypted)
	encrypted_output = f"{encrypted[:-1]}"

	last_output = ""
	final_output = ""

	for i in encrypted_output:
		last_output += str(ord(i))


	for i in last_output:
		final_output += chars[int(i)]

	# print(last_output)
	# print(final_output)
	return final_output


# print(encrypter("admin"))



# 1:26:11:28:5:30:3:32:8:33:15:34:0:38:22:41:2:43:16:44:6:45:17:52:18:61:20:66
