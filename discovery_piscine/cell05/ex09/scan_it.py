#!/usr/bin/python3
import sys

if len(sys.argv[1:]) == 2:
    check = sys.argv[1]
    count = 0
    ary = sys.argv[2].split(" ")
    for i in ary:
        if i  == check:
            count+=1
    print(count)
else:
    print("none")