#14/4/24 - Conditional statement

def checkeven(no):
    if(no%2==0):                    #colon dila aahe
        print("it is even number")
    else:
        print("it is odd number")
    
def main():
    print ("Enter a number : ")
    a = int(input())
    checkeven(a)

main()