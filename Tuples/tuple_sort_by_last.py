# Q: Write a Python program to sort a list of non-empty tuples
# in ascending order by the last element in each tuple.

tuples_list = [(1, 5), (3, 2), (2, 4), (4, 3), (5, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[-1])

print("Original List:", tuples_list)
print("Sorted List:", sorted_list)
