#!/usr/bin/python3
print("Enter the first number:")
num = int(input())
print("Enter the second number:")
num2 = int(input())
cal = num * num2
if cal < 0:
    result = "The result is negative."
elif cal > 0:
    result = "The result is positive."
else:
    result = "The result is positive and negative."

print(num , "x", num2, "=", cal)
print(result)