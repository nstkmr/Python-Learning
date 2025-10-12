file = open ("file101.txt", "r")
print(list(file))
file.close()

file = open ("file101.txt", "r")
for line in file:
    print(line)
file.close()