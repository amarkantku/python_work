# 1. How would you confirm that 2 strings have the same identity?

name1 = 'amarkant'
name2 = 'amarkant'

print(name1 is name2) # True
print(id(name1), id(name2))
print('-------------------')

name1 = 'amarkant1'
name2 = 'amarkant'

print(name1 is name2) # False
print(id(name1), id(name2))
print('-------------------')

animals = ['python','gopher']
animal1 = animals
even_more_animals = ['python','gopher']

print(animals is animal1) # True
print(id(animals), id(animal1))
print('-------------------')

print(animals is even_more_animals) # False
print(id(animals), id(even_more_animals))
print('-------------------')

# 2. How would you check if each word in a string begins with a capital letter?
print( 'The Hilton'.istitle() ) #=> True
print( 'The dog'.istitle() ) #=> False
print( 'sticky rice'.istitle() ) #=> False
print('-------------------')

# 4. Find the index of the first occurrence of a substring in a string
#There are 2 different functions that will return the starting index, find() and index(). They have slightly different behaviour.
#find() returns -1 if the substring is not found.
#'The worlds fastest plane'.find('plane') #=> 19
#'The worlds fastest plane'.find('car') #=> -1
#index() will throw a ValueError.
#'The worlds fastest plane'.index('plane') #=> 19
#'The worlds fastest plane'.index('car') #=> ValueError: substring not found

print("Find the index of the first occurrence of a substring".find('index')) # good option
print("Find the index of the first occurrence of a substring".index('index'))
print('-------------------')

text = 'hello world'
print(text[::-1])