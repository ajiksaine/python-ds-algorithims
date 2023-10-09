

def search(my_list,target):
    """
    Linear Search Algorithim

    Check if list is empty then retun None
    Check if the value at the first position in the list and compare it with the target.
    If the value at the first position is equal to the target, return the index.
    Else check the next item on the list until you find the value or reach the end of the list.
    If you find the value return the position
    Otherwise return None

    Work implementation

    loop through the list and compare the value with the target until you find the value or reach the end of the list
    if you find the value return the position of the value
    else if it is the end of the list and it is not the value, return None

    This have a time complexcity of O(n)
    Space complexcity of O(1)
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

input_list = [1,2,3,4,5,6,7,8,9,10]

verify(search(input_list,7))