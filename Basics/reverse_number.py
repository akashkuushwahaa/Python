# Q: Write a Python program to reverse a number.

n = 12345
rev = 0

# Extract digits from last and build reverse
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reversed number:", rev)
