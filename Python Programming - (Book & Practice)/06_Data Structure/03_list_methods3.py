list = [0,1,2,3,1,4,5,6,7,9,8,4]

list.pop(4) # It deletes the object at specified index if not specified it will delete the last object 
print(list)

list.remove(4) # Deletes the first occurence of that object
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list2 = [1,2,3,4,5,6]
list3 = [0,1,2,3]

list2.extend(list3)
print(list2)

list2[6:] = [] # It deletes the objects from the index 6 to the end
print(list2)