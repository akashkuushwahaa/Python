tuples = [(1, 5), (3, 2), (2, 4), (4, 3), (5, 1)]
sorted_list = sorted(tuples, key=lambda x: x[-1])
print(sorted_list)
