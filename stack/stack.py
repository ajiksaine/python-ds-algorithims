class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # Create a node with the data
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        # Set the created node to the top node
        self.top = new_node
        # Increase the size of the stack by one
        self.size += 1