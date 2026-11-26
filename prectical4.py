
import numpy as np

# 1. Batch Information
batch = input("Enter Batch Name: ")
batch = batch.strip()

department = batch.split("-")[-1].replace("_", " ")

# 2. Subjects in Tuple
subjects = ("Python", "Java", "DBMS", "Maths", "BigData")

# 3. Student Names in List
students = []

for i in range(10):
    name = input("Enter Student Name: ")
    students.append(name)

# 4. Roll Numbers
print("\nStudent Details:")

for i in range(10):
    print(i+1, students[i])

# 5. Enter Marks
marks = []

for i in range(10):
    print("\nEnter marks for", students[i])
    row = []

    for j in range(5):
        m = int(input("Enter marks: "))
        row.append(m)

    marks.append(row)

# Convert into NumPy Array
marks = np.array(marks)

# 6. Total and Percentage
total = np.sum(marks, axis=1)
percentage = total / 5

print("\nTotal and Percentage:")

for i in range(10):
    print(students[i], total[i], percentage[i])

# 7. Subject Average
avg = np.mean(marks, axis=0)

for i in range(5):
    print(subjects[i], "Average:", avg[i])

# 8. Highest and Lowest Marks
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# 9. Highest and Lowest Student
high = np.argmax(total)
low = np.argmin(total)

print("Highest Student:", students[high])
print("Lowest Student:", students[low])

# 10. Class Average
class_avg = np.mean(percentage)
print("Class Average:", class_avg)

# 11. Highest and Lowest Subject Average
print("Highest Subject:", subjects[np.argmax(avg)])
print("Lowest Subject:", subjects[np.argmin(avg)])

# 12. Slicing
print("\nFirst 3 Students - Last 2 Subjects:")
print(marks[:3, -2:])

# 13. Search Subject
search = input("\nEnter Subject Name: ")

if search in subjects:
    print("Subject Found at Index:", subjects.index(search))
else:
    print("Subject Not Found")

# 14. Distinction Students
distinction = []

for i in range(10):
    if percentage[i] >= 85:
        distinction.append(students[i])

print("Distinction Students:", distinction)

# 15. Failed Students
failed = []

for i in range(10):
    if np.any(marks[i] < 40):
        failed.append(students[i])

print("Failed Students:", failed)

# 16. Above Class Average
print("\nStudents Above Class Average:")

for i in range(10):
    if percentage[i] > class_avg:
        print(students[i])

# 17. Reverse Names
print("\nReverse Names:")
print(students[::-1])

# 18. Alphabetical Order
print("\nAlphabetical Names:")
print(sorted(students))

# 19. Final Report
print("\n===== ACADEMIC REPORT =====")

print("Batch Name:", batch)
print("Department:", department)
print("Total Students:", len(students))
print("Class Average:", round(class_avg, 2), "%")
print("Highest Student:", students[high])
print("Lowest Student:", students[low])
print("Highest Subject:", subjects[np.argmax(avg)])
print("Lowest Subject:", subjects[np.argmin(avg)])
print("Distinction Count:", len(distinction))
print("Failed Count:", len(failed))

print("===========================")
