from binary_tree import BinaryTree

def find_sum(current_node):
    """
    sum all the numbers in a binary tree
    ie. given a given node the sum is data plus the sum of all the nodes in the left sub tree 
    and the sum of all the nodes in the right sub tree
    """

    if current_node is None:
        return 0
    else:
        return current_node.data + find_sum(current_node.left) + find_sum(current_node.right)
    

T1 = BinaryTree()
T1.insert(100)
T1.insert(90)
T1.insert(60)
T1.insert(80)
T1.insert(70)
T1.insert(50)
T1.insert(200)
T1.insert(250)
T1.insert(220)

sum = find_sum(T1.root_node)
print("Sum of all Nodes in T1 is: ",sum)
