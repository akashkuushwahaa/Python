# Q: Enter a decimal number and display its binary equivalent.

n = 13
binary = ""

while n > 0:
    binary = str(n % 2) + binary  # remainder gives binary digit
    n //= 2

print("Binary equivalent:", binary)
