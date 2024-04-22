# variable number of arguments (rest parameters)

#-------------------------- Fixed number of parameters---------------
def Addition(no1, no2, no3, no4):
    ans = no1+no2+no3+no4
    return ans

print(" Addition is ", Addition(10,20,30,40))


#-------------------------- variable number of parameters---------------

def Addition(*no):
    print(type(no))
    print(len(no))
    ans = 0
    for i in no:
        ans = ans + i
    return ans

Result = Addition(20,10,30)
print(Result)   

Result = Addition(20,10,30,40,50)
print(Result)   