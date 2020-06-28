#! /usr/bin/python

test_str = "label"
arr = []

for i in test_str:
    token = int(ord(i)) ^ 13
    token = chr(token)
    arr.append(token)

print(''.join(arr))