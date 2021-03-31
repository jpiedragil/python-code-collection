# time_testing.py
#
# Memory usage comparison between an OrderedDict and a regular dict.
#

import sys
from collections import OrderedDict

ordereddict_memory = sys.getsizeof(OrderedDict.fromkeys(range(1000)))
dict_memory = sys.getsizeof(dict.fromkeys(range(1000)))

gain = 100 - dict_memory / ordereddict_memory * 100

print(f"OrderedDict: {ordereddict_memory} bytes")
print(f"dict: {dict_memory} bytes ({gain:.2f}% lower)")
