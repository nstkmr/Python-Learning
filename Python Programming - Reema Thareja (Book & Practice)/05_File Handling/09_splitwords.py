with open("file101.txt", "r") as file:
    line = file.readline()
    words = line.split()
    #words = line.split(',') #Only splits when comma is encountered

    print(words)
