#! /usr/bin/python

x = int(input("0 or 1\n"))
arr2 = []

if x == 0:
    arr = [100, 101, 102, 101, 110, 101, 115, 116, 114, 97, 116, 101]
elif x == 1:
    arr = ['h', 'a', 'c', 'k', 'e', 'r', 'm', 'a', 'n']
else:
    exit()

for y in arr:
    if x == 0:
        token = chr(y)
    else:
        token = ord(y)
    arr2.append(token)

if x == 0:
    print(''.join(arr2))
else:
    print(arr2)