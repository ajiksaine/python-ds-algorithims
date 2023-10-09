def search(input_list, target):
    """
    Pre Condition 
    The input list has to be sorted

    Binary Search Algorithim

    Check if list is empty then retun None
    Define the first and last position of the list
    Check if the mid point value is equal to the target, then return the midpoint
    Otherwise check if the value at midpoint is less than the target, slice the list by 1/2 and only consider the second 
    half by setting first to midpoint +1 
    Otherwise if the value at midpoint is grater than the target, slice the list by 1/2 and only consider the first 
    half of the list by setting last to midpoint -1
    Keep looping through the new list eachtime and repeat from step 3 until you find the value
    If the value is not found untill first == last then terminate the loop and return None
    """
    if(len(input_list) <= 0):
        return None
    
    first = 0
    last = len(input_list)-1
    
    while(first <= last):
        midpoint = (first+last)//2

        if(input_list[midpoint]==target):
            return midpoint
        elif(input_list[midpoint] < target):
            first = midpoint +1
        else:
            last = midpoint -1

    return None

def verify(result):
    if result is not None:
        print("Target found at position: ", result)
    else:
        print("Target not in the given list")

# Get user input for the sorted array
input_str = input("Enter an array of sorted numbers, separated by spaces: ")
input_list = [int(x) for x in input_str.split()]



while True:
    # Get user input for the target element to search
    target = input("Enter the target element to search for (or exit to quit): ")

    if str(target) == "exit":
        break

    key = int(target)

    verify(search(input_list,key))