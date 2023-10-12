class Node():
    """
    Node class used to create a binary tree
    model 3 attributes: data left node and right node
    """
    data = None
    left = None
    right = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class BinaryTree():
    """
    Binary tree data structure
    Keep reference of the root node which can be used to navigate to every other node in the tree
    """
    root_node = None
    
    def __init__(self):
        self.root_node = None

    def insert(self,data):
        """
        Inserts data into the binary tree using the _insert_recusively function
        """
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            self._insert_recusively(self.root_node,data)

    def _insert_recusively(self,current_node,data):
        """
        Inserts data into the binary tree recusively by checking if the data to be inserted is less than the root node,
        it insert into the left side of the tree, otherwise it is grater, it inserts into the right side of the tree 
        """
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recusively(current_node.left,data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recusively(current_node.right,data)

    def insert_with_loop(self,data):
        """
        Inserts data into the binary tree using loops.It checks if the data to be inserted is less than the root node,
        it insert into the left side of the tree, otherwise it is grater, it inserts into the right side of the tree 
        """
        current_node = self.root_node
        if current_node is None:
            self.root_node = Node(data)
            return
        
        while current_node is not None:
            if data < current_node.data:
                previous_node = current_node
                current_node = current_node.left 
            elif data > current_node.data:
                previous_node = current_node
                current_node = current_node.right

        if data < previous_node.data:
            previous_node.left = Node(data)
        else:
            previous_node.right = Node(data)
        