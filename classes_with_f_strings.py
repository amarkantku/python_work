class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} old. Surprise!"

comedian =  Comedian("Amarkant", "Kumar", "33")
print(f"{comedian}")
print(f"{comedian!r}")

''' you’ll need to make sure you include at least one of those methods in your class definition. If you have to pick one, go with __repr__() because it can be used in place of __str__().

The string returned by __str__() is the informal string representation of an object and should be readable. The string returned by __repr__() is the official representation and should be unambiguous. Calling str() and repr() is preferable to using __str__() and __repr__() directly.

By default, f-strings will use __str__(), but you can make sure they use __repr__() if you include the conversion flag !r:'''