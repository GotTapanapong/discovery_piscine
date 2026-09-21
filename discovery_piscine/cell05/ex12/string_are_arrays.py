#!/usr/bin/python3
import sys
count = 0
if len(sys.argv[1:]) == 1:
    ary = sys.argv[1].split(" ")
    for i in sys.argv[1]:
        text = i.split()
        for j in text:
            if j == "z":
                count += 1
    if count >= 1:
      print("z"*count)
    else:
      print("none")
else:
    print("none")

