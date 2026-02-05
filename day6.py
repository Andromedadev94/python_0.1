class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def talk(self):
        print(f"Hi, my name is {self.name} and I'm {self.age}!")


p1=Person("Ali", 23)
p1.talk()

#inherites
class Animals:
    def bark(self):
        print("Bark!")


class Cat(Animals):
    pass    #just so that python doesn't like empty after a class


class Dog(Animals):
    pass

cat1=Cat()
dog1=Dog()
cat1.bark()
dog1.bark()

#importing a module
from day3 import greater_num
our_list=[4,55,2,3,122,5,33,78]
max1=greater_num(our_list)
print(max1)

#or
import day3
our_list=[4,55,2,3,122,5,33,78]
x=day3.greater_num(our_list)
print(x)
#or
import mymoduls.greater
our_list=[4,55,2,3,122,5,33,78]
x=mymoduls.greater.greater_num(our_list)
print(x)
#or
from mymoduls.greater import greater_num #foulder need to be inside new the file we executing
our_list=[4,55,2,3,122,5,33,78]
biggest=greater_num(our_list)
print(biggest)

#to call built in python modules
import random
x=random.randrange(10,30)
print(x)


import random
class Dice:
    def roll(self):
        first_num=random.randint(0,100)
        second_num=random.randint(0,100)
        return (first_num, second_num)


roll1=Dice()
print(roll1.roll())





