#module demonstration - all import

import module_marvelous

def main():
    print ("Enter first number: ")
    A = int(input())
    print ("Enter Second Number: ")
    B = int(input())

    ans = module_marvelous.Addition(A,B)     #module name need to be mentioned
    print("Addition is: ", ans)
   
    ans = module_marvelous.Multiplication(A,B)   
    print("Multiplication is: ", ans)

main()