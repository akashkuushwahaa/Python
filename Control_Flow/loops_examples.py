# Q: Demonstrate loops with examples

# Factorial using while loop
n = 5
fact, i = 1, 1
while i <= n:
    fact *= i
    i += 1
print("Factorial of", n, "is", fact)

# Sum of first n natural numbers
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of first", n, "numbers is", total)

# Multiplication table using for loop
num = 7
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    