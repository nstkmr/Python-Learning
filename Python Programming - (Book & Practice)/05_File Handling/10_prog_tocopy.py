with open("file101.txt","rb") as file1:
    with open("file102.txt","wb") as file2:
        buf = file1.read(10)
        file2.write(buf)
print("File copied!")
