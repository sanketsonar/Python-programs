#14/4/24 

def checkeven(no):
    if(no%2==0):                    #colon dila aahe
        print("it is even number")
    else:
        print("it is odd number")
    
def main():
    print ("Enter a number : ")
    a = int(input())
    checkeven(a)

# starter
if __name__ =="__main__":
    main()