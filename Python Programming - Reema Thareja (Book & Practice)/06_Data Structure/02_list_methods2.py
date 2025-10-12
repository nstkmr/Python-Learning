list = [1,"Nishant",[1,2,3,4],5,9,[2,3]]

print(list[2][1]) # To print the value in the nested list

print('a' in ['a','e','i','o','u'])

list2 = [1,4,5,2,3,8,9,4]
print(max(list2))
print(min(list2))
print(sum(list2))

list3 = sorted(list2) # We can sort the list but it has to be stored in another variable
print(list3)

print(list2.count(4))
print(list2.index(4)) # At which index the number 4 first appear

list2.insert(3,5) # We can insert a element in between the list
print(list2)