#A basic print function
print("Hello World!")

#Varibles
a = 20
b = 50
sum = a + b
print("The sum of a and b is", sum)

#Varibles Error
age = 20
age_text = "years old"
#print(age, age_text)
#It should be:
print(str(age), age_text)

#User Input + Capitalize
input1 = input("Give me your name! ")
input2 = input("Give me your gender! ")
print("\nResults of "+ input1.capitalize() + "\n-----------------------------\nGender: " + input2.capitalize())

#Title
title = "timo happy shop"
print("\n\nWelcome to", title.title())
item1 = "bread $100"
print(item1.capitalize())
item2 = "apple $500"
print(item2.capitalize())
item3 = "poop $31230"
print(item3.capitalize())
item4 = "timo $2"
print(item4.capitalize())

#Ending
print("\nThis is the end of day 1, hope you have a better day tomorrow!")
