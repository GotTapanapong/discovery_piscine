#!/usr/bin/python3
import sys
list = list()
if len(sys.argv[1:]) == 2:
    for i in range(int(sys.argv[1]),int(sys.argv[2])+1,1):
        list.append(i)
    print(list)
else:
    print("none")