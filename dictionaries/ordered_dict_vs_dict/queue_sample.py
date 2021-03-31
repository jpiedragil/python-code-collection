# sample_queue.py
#
# Usage examples for Queue class.

from queue import Queue

# Create an empty queue
#
empty_queue = Queue()
print(empty_queue)

# Create a queue with initial data
#
numbers_queue = Queue([("one", 1), ("two", 2)])
print(numbers_queue)

# Create a queue with keyword arguments
#
letters_queue = Queue(a=1, b=2, c=3)
print(letters_queue)

# Add items
#
numbers_queue.enqueue(("threee", 3))
print(numbers_queue)

# Remove items
#
numbers_queue.dequeue()
print(numbers_queue)

# Remove items
#
numbers_queue.dequeue()
print(numbers_queue)

# Remove items
#
numbers_queue.dequeue()
print(numbers_queue)

# Remove items
#
numbers_queue.dequeue()
print(numbers_queue)
