# Q: Write a Python Program to generate dictionary that contains
# numbers between 1 and n in the form (x, x*x).
# Print the dictionary.

n = 5
square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x  # key=x, value=x squared

print("Generated dictionary:", square_dict)
