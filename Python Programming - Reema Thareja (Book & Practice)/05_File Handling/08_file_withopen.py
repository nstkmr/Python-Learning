with open("file101.txt", "rb") as file:
    for line in file:
        print(line)

print("To check if the file is closed: ",file.closed) # The 'with' keyword automatically close the file without the file.close() function