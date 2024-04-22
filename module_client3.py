#module demonstration

import module_marvelous as m    #alias - shortning module name as 'm'

def main():
    print ("Enter first number: ")
    A = int(input())
    print ("Enter Second Number: ")
    B = int(input())

    ans = m.Addition(A,B)           # module name is mentioned
    print("Addition is: ", ans)
   
    ans = m.Multiplication(A,B)
    print("Multiplication is: ", ans)

main()