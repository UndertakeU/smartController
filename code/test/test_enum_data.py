from enum import Enum

class Animal(Enum):
	ant = 1
	dog = 2

c = Animal(2)
print (c)

for i in Animal:
	print (i)