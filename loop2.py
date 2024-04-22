def display(Cnt):
    i = 0
    if(Cnt<=0):
        print(" Invalid Input ")
        return

    while(i<Cnt):                           # using while
        print(" Jay Ganesh....", end =" ")  # for no new line
        i = i + 1
    print ("")

    for i in range(Cnt):                    # using for
        print(" Jay Ganesh...", end = " ") 

def main():
    no = int(input(" Enter frequency: "))
    display(no)

if __name__ == "__main__":
    main()    
