#! /bin/python3

import base64

fp = open("b64.txt", "rb")
d_data = fp.read()

for i in range(0, 50):
    print("Count: ", i)
    d_data = base64.b64decode(d_data)
print(d_data)

fp.close()