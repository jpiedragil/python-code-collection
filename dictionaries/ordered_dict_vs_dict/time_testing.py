# time_testing.py
#
# Performance comparison between an OrderedDict and a regular dict.
#

from collections import OrderedDict
from time import perf_counter


def average_time(dictionary):

    time_measurements = []

    for _ in range(1_000_000):

        start = perf_counter()
        dictionary["key"] = "value"
        "key" in dictionary
        "missing_key" in dictionary
        dictionary["key"]
        del dictionary["key"]
        end = perf_counter()

        time_measurements.append(end - start)

    return sum(time_measurements) / len(time_measurements) * int(1e9)


ordereddict_time = average_time(OrderedDict.fromkeys(range(1000)))
dict_time = average_time(dict.fromkeys(range(1000)))

gain = ordereddict_time / dict_time

print(f"OrderedDict: {ordereddict_time:.2f} ns")
print(f"dict: {dict_time:.2f} ns ({gain:.2f}x faster)")
