# Q: Write a Python program to print Fibonacci series up to n terms.

n = 7
a, b = 0, 1

print("Fibonacci series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
