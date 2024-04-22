#14/04/24 - defining main function

def Addition(No1, No2):
    print("Inside addtion function ")
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Inside main function ")
    print ("Enter first number : ")
    A = int(input())

    print ("Enter second number :")
    B = int(input())

    Result = Addition(A,B)

    print("Addition is : " , Result)

main() # execution starts from here
print("End of application")



#execution sequence - 21-9-10-11-12-14-15-17-3-4-5-6-7-17-19-21-22