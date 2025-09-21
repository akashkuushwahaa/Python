# Q: Write a Python program to find factorial of a number using loop.

n = 5
fact = 1

# Multiply numbers from 1 to n
for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)
