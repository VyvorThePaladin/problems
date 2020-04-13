import base64

plaintext = b'cool for the summer'
b64text = b'ZGVtaSBsb3ZhdG8='

print(base64.b64encode(plaintext).decode('ascii'))
print(base64.b64decode(b64text).decode('ascii'))

