import os
print("Current working directory is....", os.getcwd())
os.chdir("New dir")
print("After chdir, the current directory is now....", end=' ')
print(os.getcwd())