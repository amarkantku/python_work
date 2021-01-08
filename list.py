''' List is a ordered collection data type in python, it is dynamic and mutable in nature'''

cars = ['suzuki', 'ford', 'maruti', 'audi', 'auddi', 'toyota']
print(cars);

# append a new car in list
cars.append('honda')
print(cars);

# insert to a specific position
cars.insert(1,'tata');
print(cars);

#remove item from list
del cars[0]
print(cars)

car = cars.pop() # remove form last index
print(cars)

cars.remove('ford')
print(cars)

#sort
cars.sort();
print(cars)
