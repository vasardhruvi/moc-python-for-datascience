names = []
marks = []

for i in range(10):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    names.append(name)
    marks.append(mark)

marks_tuple = tuple(marks)

student = {}
for i in range(10):
    student[names[i]] = marks[i]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / 10

print("\nMarks List:", marks)
print("Marks Tuple:", marks_tuple)
print("Student Dictionary:", student)

print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)

print("\nStudents Scoring Above Average:")
for i in range(10):
    if marks[i] > average:
        print(names[i], ":", marks[i])

unique_marks = set(marks)
print("\nUnique Marks:", unique_marks)
