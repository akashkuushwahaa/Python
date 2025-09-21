# Q: Print the following pattern using for loop
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()
