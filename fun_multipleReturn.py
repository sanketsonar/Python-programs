#14/04/24 - one function returning multiple values

def Calculations (No1,No2):
    Add = No1 + No2
    Sub = No1 - No2
    return Add, Sub  #multiple returns

print("Enter first number : ")
A= int(input())

print("Enter second Number : ")
B = int(input())

Result1, Result2 = Calculations(A,B) #catching multiple return values

print("Addition is : ", Result1)
print("Substraction is : ", Result2)
