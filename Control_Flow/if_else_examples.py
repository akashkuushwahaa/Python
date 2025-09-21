# Q: Demonstrate simple if-else programs

# Check positive/negative
n = -5
if n >= 0:
    print(n, "is Positive")
else:
    print(n, "is Negative")

# Largest of three numbers
a, b, c = 12, 25, 7
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Even or odd
num = 10
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
