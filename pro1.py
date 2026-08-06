

name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
age = int(input("Enter Age: "))

print("\nEnter marks for 5 subjects:")
mark1 = float(input("english: "))
mark2 = float(input("gujrati: "))
mark3 = float(input("hindi: "))
mark4 = float(input("maths: "))
mark5 = float(input("Science: "))

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

