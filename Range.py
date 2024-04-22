# Range function in python -

# range(start, end, displacement)
# start is by default 0 if not mentioned
# displacement is bydefault 1
# end should be mentioned explicitely (it gets excluded - last item not displayed)

Arr = range(5)
print(Arr)           # range(0, 5)
print(range(5))      # range(0, 5)

Arr = list(range(5))
print(Arr)                  # [0, 1, 2, 3, 4]
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(3,8)))     # [3, 4, 5, 6, 7] 
print(list(range(3,12,2)))  # [3, 5, 7, 9, 11]
print(list(range(20,1,-1))) # decrement - [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]