def max(numbers):  # global namespace
    print("USER DEFINED FUNCTION MAX.....")
    large = -1  # local namespace
    for i in numbers:
        if i > large:
            large = i
    return large

numbers = [9, -1, 4, 2, 7]
print(max(numbers))
print("Sum of these numbers = ", sum(numbers))  # built-in namespace
