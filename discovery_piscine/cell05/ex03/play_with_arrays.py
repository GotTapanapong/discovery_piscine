#!/usr/bin/python3
ori_ary = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()
for i in ori_ary:
    if i+2 >= 10:
        new_set.add(i+2)

print(ori_ary)
print(new_set)
