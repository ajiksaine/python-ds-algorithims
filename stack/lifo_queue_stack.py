# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get()