# queue.py
#
# Sample dictionary-based queue system.
#
from collections import OrderedDict


class Queue:

    def __init__(self, initial_data=None, /, **kwargs):

        self.data = OrderedDict()

        if initial_data is not None:

            self.data.update(initial_data)

        if kwargs:

            self.data.update(kwargs)

    def enqueue(self, item):

        key, value = item

        if key in self.data:

            self.data.move_to_end(key)

        self.data[key] = value

    def dequeue(self):

        try:

            return self.data.popitem(last=False)

        except KeyError:

            print("Empty queue")

    def __len__(self):

        return len(self.data)

    def __repr__(self):

        return f"Queue({self.data.items()})"
