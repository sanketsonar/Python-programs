#module demonstration 

from module_marvelous import Addition, Multiplication   #- specific import
# from module_marvelous import Multiplication

def main():
    print ("Enter first number: ")
    A = int(input())
    print ("Enter Second Number: ")
    B = int(input())

    ans = Addition(A,B)                             #module name not mentioned  
    print("Addition is: ", ans)
   
    ans = Multiplication(A,B)
    print("Multiplication is: ", ans)

main()