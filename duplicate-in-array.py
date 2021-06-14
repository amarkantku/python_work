a_lsit = [1,2,3,4,5,2,4,3]

for i in a_lsit:
	if a_lsit.count(i) > 1:
		a_lsit.remove(i)
print(a_lsit);

a_lsit = [1,2,3,4,5,2,4,3]
a_lsit.sort()

prev = a_lsit[0]
for i in range(1, len(a_lsit)):
	if(prev == a_lsit[i]):
		a_lsit[i] = 0
	else:
		prev = a_lsit[i]

print(list(filter(bool,a_lsit)))
a_lsit = [1,2,3,4,5,2,4,3]

print(dict.fromkeys(a_lsit))
print(dict.fromkeys(a_lsit).keys())
print(list(dict.fromkeys(a_lsit).keys()))

