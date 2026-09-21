#!/usr/bin/python3
num = input("Give me a number: ")

if float(num)%1 > 0:
    print("This number is a decimal.")
else:
    print("This number is an integer.")