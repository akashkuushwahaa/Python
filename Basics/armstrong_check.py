num = 153
temp = num
result = 0
while temp > 0:
    digit = temp % 10
    result += digit ** 3
    temp //= 10
print("Armstrong" if result == num else "Not Armstrong")
