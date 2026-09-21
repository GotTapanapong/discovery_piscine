#!/usr/bin/python3
age = int(input("Please tell me your age: "))
print("You are currently %d years old."%age)
for i in range(10, 40 ,10):
    print("In %d years, you'll be %d years old."%(i,age+i))
