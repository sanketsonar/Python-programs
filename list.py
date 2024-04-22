# list in python 
#  heterogenous
#  Ordered
#  Indexed
#  Mutable - Changeble
#  Allows Duplicate
#  it uses square [] brackets

Arr1 = [10,20,30,40]
print(type(Arr1))

Arr2 = [11, 23, "Radhe", True, 11.31, 11]
print(Arr2)
print("Length of list is: ", len(Arr2))

print(Arr2[3])
print(Arr2[4])
Arr2[4] = 3.15
print(Arr2) 

Arr2.append(51)     # insert new element at end of list
print(Arr2) 
print("Length of list is: ", len(Arr2))

