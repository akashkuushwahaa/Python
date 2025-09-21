# Q: Demonstrate break and continue in loops

# Break example
for i in range(1, 6):
    if i == 3:
        break   # exits loop when i=3
    print("Break Example:", i)

# Continue example
for i in range(1, 6):
    if i == 3:
        continue   # skips printing 3
    print("Continue Example:", i)
