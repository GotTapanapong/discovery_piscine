#!/usr/bin/python3
import sys
if len(sys.argv[1:]) > 1:
    for i in range(len(sys.argv[1:]), 0 ,-1):
        print(sys.argv[i])
else:
    print("none")