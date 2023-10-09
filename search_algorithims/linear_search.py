

def search(my_list,target):
    """
    Linear Search Algorithim

    Check if the value at the first position in the list and compare it with the target.
    If the value at the first position is equal to the target, return the index.
    Else check the next item on the list until you find the value or reach the end of the list.
    If you find the value return the position
    Otherwise return None

    Work implementation

    loop through the list and compare the value with the target until you find the value or reach the end of the list
    if you find the value return the position of the value
    else if it is the end of the list and it is not the value, return None

    This have a time complexity of O(n)
    Space complexity of O(1)
    """

    for n in range(len(my_list)):
        if my_list[n] == target:
            return n
    return None

def print_results(result):
    print(result)

def verify(result):
    if result is not None:
        print("Target found at position: ", result)
    else:
        print("Target not in the given list")


# Get user input for an array
input_str = input("Enter a array of numbers, separated by spaces: ")
input_list = [int(x) for x in input_str.split()]



while True:
    # Get user input for the target element to search
    target = input("Enter the target element to search for (or exit to quit): ")

    if str(target) == "exit":
        break

    key = int(target)

    verify(search(input_list,key))