# Q: Write a python program that has dictionary of names of students
# and a list of their marks in 4 subjects.
# Create another dictionary with total marks.
# Find out the topper and his score.

students = {
    "Amit": [78, 85, 90, 95],
    "Riya": [92, 88, 79, 94],
    "Rahul": [85, 87, 93, 89],
    "David": [92, 91, 85, 87]
}

# Dictionary to store total marks
total_marks = {}
for name, marks in students.items():
    total_marks[name] = sum(marks)  # sum() adds all marks

print("Total Marks of Students:", total_marks)

# Find topper → max() on dictionary with key=total
topper = max(total_marks, key=total_marks.get)
print("Topper:", topper, "with", total_marks[topper])
