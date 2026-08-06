students = []
grades = {}

subjects = ["English", "Gujarati", "Hindi", "Maths", "Science"]

for i in range(10):
    print("\nEnter Details of Student", i + 1)

    roll = int(input("Roll Number: "))

    while True:
        name = input("Name: ")
        if name.replace(" ", "").isalpha():
            break
        print("Enter only alphabets for name.")

    marks = []
    total = 0

    for subject in subjects:
        while True:
            mark = int(input(f"{subject} Marks (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                total += mark
                break
            else:
                print("Marks must be between 0 and 100.")

    percentage = total / 5

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "Roll": roll,
        "Name": name,
        "Marks": tuple(marks),
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)

    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)


print("\n--------- STUDENT DETAILS ---------")
for s in students:
    print(s)


class_avg = sum(s["Percentage"] for s in students) / len(students)
print("\nClass Average Percentage:", class_avg)


highest = max(s["Total"] for s in students)
print("\nHighest Scorer(s):")
for s in students:
    if s["Total"] == highest:
        print(s["Name"], "-", s["Total"])


lowest = min(s["Total"] for s in students)
print("\nLowest Scorer(s):")
for s in students:
    if s["Total"] == lowest:
        print(s["Name"], "-", s["Total"])


print("\nStudents Above Class Average:")
for s in students:
    if s["Percentage"] > class_avg:
        print(s["Name"])


print("\nStudents Failed in One or More Subjects:")
for s in students:
    if any(mark < 40 for mark in s["Marks"]):
        print(s["Name"])


print("\nGrade Dictionary:")
print(grades)


print("\nStudents in Alphabetical Order:")
names = [s["Name"] for s in students]

for name in sorted(names):
    print(name)


first = second = -1

for s in students:
    if s["Total"] > first:
        second = first
        first = s["Total"]
    elif s["Total"] > second and s["Total"] != first:
        second = s["Total"]


print("\nSecond Highest Scorer(s):")
for s in students:
    if s["Total"] == second:
        print(s["Name"], "-", s["Total"])


subject_avg = []

for i in range(5):
    total = 0
    for s in students:
        total += s["Marks"][i]
    subject_avg.append(total / 10)


highest_avg = max(subject_avg)
subject = subjects[subject_avg.index(highest_avg)]

print("\nSubject with Highest Average:", subject)
print("Average Marks:", highest_avg)


names = [s["Name"] for s in students]

unique = set()
duplicates = set()

for name in names:
    if name in unique:
        duplicates.add(name)
    else:
        unique.add(name)


print("\nDuplicate Student Names:")

if duplicates:
    for name in duplicates:
        print(name)
else:
    print("No Duplicate Names")