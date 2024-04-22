# addition of commandline arg
import sys

def addition(no1, no2):
    ans = no1 + no2
    return ans

def main():
    print("welcome to the application: ", sys.argv[0])

    if(len(sys.argv) != 3):
        print("invalid number of arguments")
        print(" plese provide 2 numeric argument")
        return
    
    Result = addition(int(sys.argv[1]), int(sys.argv[2]))
    print(" addition is: ", Result)

if __name__ =="__main__":
    main()    
