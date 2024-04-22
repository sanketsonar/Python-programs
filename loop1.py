def display(Cnt):
    i = 0
    if(Cnt<=0):
        print(" Invalid Input ")
        return

    while(i<Cnt):
        print(" Jay Ganesh....")
        i = i + 1
    print ("")

    for i in range(Cnt):
        print(" Jay Ganesh...")

def main():
    no = int(input(" Enter frequency: "))
    display(no)

if __name__ == "__main__":
    main()    
