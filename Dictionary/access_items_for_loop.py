# Q: With the help of example explain how to access items in a dictionary
# using a for loop.

student = {"name": "Riya", "age": 20, "marks": 88}

print("Dictionary:", student)

# Looping through key-value pairs
for key, value in student.items():
    print(key, ":", value)
