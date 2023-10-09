def search(list,key,low,high):
    """
    Pre Condition 
    The input list has to be sorted

    Binary Search Algorithim

    Check if the subset of the list passed is empty then retun None
    Check if the mid point value is equal to the target, then return the midpoint
    Otherwise check if the value at midpoint is less than the target, only consider the second half 
    by setting low to midpoint +1 and calling the search function on itself
    Otherwise if the value at midpoint is grater than the target, only consider the first half of the list by setting 
    last to midpoint -1 and calling the search function on itself
    
    """

    if low > high:
        return None
    
    mid = (low+high)//2

    if list[mid] == key:
        return mid
    elif list[mid] < key:
        return search(list,key,mid+1,high)
    else:
        return search(list,key,low,mid-1)
    

def verify(key,result):
    if result is not None:
        print(f"{key} found at position: {result}")
    else:
        print(f"{key} not in the given list")



# Get user input for the sorted array
input_str = input("Enter a sorted array of numbers, separated by spaces: ")
input_list = [int(x) for x in input_str.split()]



while True:
    # Get user input for the target element to search
    target = input("Enter the target element to search for (or exit to quit): ")

    if str(target) == "exit":
        break

    key = int(target)

    verify(key,search(input_list,key,0,len(input_list)-1))
    