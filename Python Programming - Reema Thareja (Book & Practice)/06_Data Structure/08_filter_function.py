def check(x):
    if (x%2==0 or x%4==0):
        return 1

# Call check() for every value between 2 to 22

evens = list(filter(check, range(2,22)))
print(evens)