#!/usr/bin/python3
import sys
if len(sys.argv[1:]) >= 1:
   print("parameters:", len(sys.argv[1:]))
   for i in sys.argv[1:]:
       print("%s : %s"%(i, len(i)))
else:
    print("none")