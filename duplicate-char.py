string  = "hello how are you"
duplicate_char_map = dict()
for char in string :
	if char != ' ':
		if (duplicate_char_map.get(char) == None):
			duplicate_char_map[char] = 1
		else:
			duplicate_char_map[char] = duplicate_char_map[char] + 1  

print(duplicate_char_map)

print('------------------------')
duplicate_char_map = dict()
for char in string:
	count = string.count(char)
	if char != ' ' and count >=2 and duplicate_char_map.get(char) == None:
		duplicate_char_map[char] = count

print(duplicate_char_map)