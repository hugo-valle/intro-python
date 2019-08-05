"""
Learn about bytes.
Bytes are similar to str type, but they are a sequence of
bytes instead of Unicode code points.

Use for raw binary data, fixed-width, single-byte encoding: ASCII

Use the byte() constructor
"""
d = b'data'
print(d, type(d))

info = b'some bytes here'
# Split the bytes using split() method for bytes
print(info.split())

# Encoding: Alt+ 162 = ó
message = "Vamos al zoológico"
print(message)
# Encoded the string
data = message.encode("utf-8")
print(data)
# Decoding the string
new_message = data.decode("utf-8")
print(new_message)