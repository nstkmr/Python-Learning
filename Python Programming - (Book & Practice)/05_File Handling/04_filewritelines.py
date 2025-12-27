file = open("file101.txt", "a") # This is append mode
lines = ["Up above the world so high, like a diamond in the sky"]
file.writelines(lines)
file.close()
print("Data has been written...")
