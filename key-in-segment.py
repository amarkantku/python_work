def key_in_segment(a_list, num, windowSize):
	start, end = 0, 0
	found = False
	while end < len(a_list):
		end += windowSize
		if (num in a_list[start:end]):
			found = True
		else:
			found = False
			break
		start += windowSize
	return found

print(key_in_segment([3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3], 3, 3))
print(key_in_segment([21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25], 23, 5))
print(key_in_segment([5, 8, 7, 12, 14, 3, 9], 8, 2))