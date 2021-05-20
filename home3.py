import os

default_path = "/home/Diode/Dicot/VisionIOT/main"

if not os.path.exists(default_path):
    os.makedirs(default_path)

filename = "/main.dat"

try:
    open(default_path + filename, 'w').close()
except OSError:
    print("Couldn't create file!")
else:
    print("File created!")

file_open = open(default_path + filename, 'w')
file_open.write("abc\n")
file_open.write("123")
file_open = open(default_path + filename)
content = file_open.read()
file_open.close()
print(content)