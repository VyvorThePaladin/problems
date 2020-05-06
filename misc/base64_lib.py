#! /bin/python3

import base64

fp = open("encodedflag.txt", "rb")
d_data = fp.read()

for i in range(0, 5):
    d_data = base64.b16decode(d_data)

for i in range(0, 5):
    d_data = base64.b32decode(d_data)

for i in range(0, 5):
    d_data = base64.b64decode(d_data)
print(d_data)

fp.close()