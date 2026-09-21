#!/usr/bin/python3
import sys
if len(sys.argv[1:]) >= 1:
   for i in sys.argv[1:]:
        if i.endswith("ism"):
           continue
        else:
           print(i, end=(""))
           print("ism")
     
else:
    print("none")