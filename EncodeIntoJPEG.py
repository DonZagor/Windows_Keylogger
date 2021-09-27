with open('keylog.py', 'r') as f:
    data = f.readlines()
with open('photo.jpg', 'ab') as f:
    for line in data:
        f.write(line.encode())
