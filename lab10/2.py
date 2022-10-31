import os
#os.rename("/Users/nastya/NK/NK/lab10/fin.txt", "/Users/nastya/NK/NK/lab10/start.txt")

p = os.path.abspath('2.py ')
name = os.path.basename(p)
os.rename("/Users/nastya/NK/NK/lab10/start.txt", "/Users/nastya/NK/NK/lab10/fin.txt")

print(name)
print(p)