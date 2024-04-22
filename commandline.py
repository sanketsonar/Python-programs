# Command line arguments 
import sys          # sys - inbuilt 'systeam' module it contain 'argv' heterogenous array use to pass command line arg

def main():
    print(" Demonstration of command line arguments ")
    print(" Name of application: ", sys.argv[0])    # 0th index has name of file
    print(" Datatype of argv is: ", type(sys.argv))  # list
    print(" No of command line arguments: ", len(sys.argv))

if __name__ == "__main__":
    main()