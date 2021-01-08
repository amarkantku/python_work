people = {
	1: {'name': 'John', 'age': '27', 'sex': 'Male'},
	2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
}

print(people.items())
print(people.keys())
print(people.values())

for key, item in people.items():
	print(key)
	print(item)

