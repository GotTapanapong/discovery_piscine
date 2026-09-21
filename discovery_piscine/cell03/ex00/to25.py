#!/usr/bin/python3
print("Enter a number less than 25")
num = int(input())

if num > 25:
    print("Error")
else:
    for i in range(num, 25, 1):
        print("Inside the loop, my variable is", i)