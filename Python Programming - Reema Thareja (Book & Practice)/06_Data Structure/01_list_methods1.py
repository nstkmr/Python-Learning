list = [0,1,2,3,4,5,6,7,8,9]

print(list[2:5])
print(list[::2])

list[5] = 100 # Lists are mutable
print(list)

list.append(200)
print(list)

del list[5]
print(list)

list2 = list # Numbers will be saved in the same memory location but with diffferent names
list3 = list[:4]
print(list2)
print(list3)