name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
age = int(input("Enter Age: "))

print("\nEnter marks for 5 subjects:")

while True:
    mark1 = float(input("English: "))
    if 0 <= mark1 <= 100:
        break
    print("Marks must be between 0 and 100.")

while True:
    mark2 = float(input("Gujarati: "))
    if 0 <= mark2 <= 100:
        break
    print("Marks must be between 0 and 100.")

while True:
    mark3 = float(input("Hindi: "))
    if 0 <= mark3 <= 100:
        break
    print("Marks must be between 0 and 100.")

while True:
    mark4 = float(input("Maths: "))
    if 0 <= mark4 <= 100:
        break
    print("Marks must be between 0 and 100.")

while True:
    mark5 = float(input("Science: "))
    if 0 <= mark5 <= 100:
        break
    print("Marks must be between 0 and 100.")

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

passed = (mark1 >= 40 and mark2 >= 40 and
          mark3 >= 40 and mark4 >= 40 and
          mark5 >= 40)

print("\n========== STUDENT REPORT ==========")
print(f"Roll Number : {roll_no}")
print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"Total Marks : {total:.2f} / 500")
print(f"Percentage  : {percentage:.2f}%")

if passed:
    print("Result      : PASS")
else:
    print("Result      : FAIL")
