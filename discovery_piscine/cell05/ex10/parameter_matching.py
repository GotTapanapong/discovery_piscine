#!/usr/bin/python3
import sys
if len(sys.argv[1:]) == 1:
    word = input("What was the parameter? ")
    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")