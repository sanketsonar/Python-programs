#accepting input into list and performing operations 

def Addition(arr):
    ans = 0

    for i in data:
        ans = ans + i

    # for i in range(len(arr)):
    #     ans = ans + (arr[i])
    
    return ans

def main():
    print(' Enter no of elements you want to insert into list')
    size = int(input())
    
    arr = list()           # creating object of list - same as arr = []

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        arr.append(no)

    print(" list you enter is: ", arr)
    result = Addition(arr)
    print(" Sum of list element is: ", result)

if __name__ == "__main__":
    main()