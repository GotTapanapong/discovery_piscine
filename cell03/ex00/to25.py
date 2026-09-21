start = int(input("Enter a number less than 25: "))

if start < 25:
    i = start
    while i <= 25:
        print("Inside the loop, my variable is " + str(i))
        i += 1
else:
    print("Error")
