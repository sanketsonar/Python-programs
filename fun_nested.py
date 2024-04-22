#14/04/24 - nested function

def Calculations (No1,No2):
    def Addition(X,Y):              #function inside a function
        return X+Y
    def Substraction (X,Y):
        return X-Y
    Ans1 = Addition(No1,No2)
    Ans2 = Substraction(No1, No2)
    return Ans1, Ans2

print("Enter first number : ")
A= int(input())

print("Enter second Number : ")
B = int(input())

Result1, Result2 = Calculations(A,B) 

print("Addition is : ", Result1)
print("Substraction is : ", Result2)
