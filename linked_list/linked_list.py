class Node():
    """
    An Object for storing a single node in a linked list
    Models two arttribute data and the link to the next node on the list
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data

class LinkedList():
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of Nodes in the list
        To get the size, start from head and loop through each node to get the next node until you reach the tail node.
        Increment count by 1 each time you loop through a node
        runs in linear time ie. O(n)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self,data):
        """
        Adds new node to the head of the list
        runs in constant time ie. O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing the data that matches the key
        It returns the Node or None if the key is not found
        Loop through each node in the list until you find key in data or hit the end of the list
        
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self,data,index):
        """
        Inserts a node at a given position in the list
        Takes lenear time O(n) because while insearting the note tales O(1), finding the note at a given position takes O(n)
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index
            while position > 1:
                current = current.next_node
                position -= 1
            
            previous_node = current
            next_node = current.next_node
            previous_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Remove the node with data that maches the key or none if not found
        Takes O(n)
        """
        current = self.head
        previous_node = None
        found = False
        while current and not found:
            if current is self.head and current.data == key:
                self.head = current.next_node
                found = True
            elif current.data == key:
                previous_node.next_node = current.next_node
                found = True
            else:
                previous_node = current
                current = current.next_node

        return current
    
    def remove_at_index(self,index):
        """
        Remove the node at a given index in the list
        takes O(n) time
        """
        current = self.head
        
        if index == 0:
            self.head = current.next_node

        if index > 0:
            previous_node = None
            position = index
            while position > 0:
                previous_node = current
                current = current.next_node
                position -= 1
            previous_node.next_node = current.next_node


    def get_node_at_index(self,index):
        """
        Read the node at a given index in the list
        Takes O(n)
        """
        current = self.head
        if index == 0:
            return self.head
        
        if index > 0:
            position = index
            while position > 0:
                position -= 1
                current = current.next_node
            return current
                    

    def __repr__(self) -> str:
        """
        returns the string representation of the list
        takes linear time O(n)
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)


    