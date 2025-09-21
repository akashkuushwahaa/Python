# Q: Write a python program that generates a set of prime numbers and another
# set of odd numbers. Demonstrate union, intersection, difference, and
# symmetric difference.

prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
odd_set = {x for x in range(1, 21, 2)}

print("Prime set:", prime_set)
print("Odd set:", odd_set)
print("Union:", prime_set | odd_set)
print("Intersection:", prime_set & odd_set)
print("Difference:", prime_set - odd_set)
print("Symmetric Difference:", prime_set ^ odd_set)
