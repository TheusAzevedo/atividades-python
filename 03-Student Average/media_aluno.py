print("=" * 50)
print("STUDENT GRADE SYSTEM")
print("=" * 50)

name = input("Enter student's name: ")
grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("\n" + "=" * 50)
print(f"STUDENT: {name}")
print(f"GRADES: {grade1:.1f}, {grade2:.1f}, {grade3:.1f}")
print(f"AVERAGE: {average:.2f}")

if average >= 7.0:
    situation = "APPROVED"
    message = "Congratulations! You passed!"
elif average >= 5.0:
    situation = "RECOVERY"
    message = "You are in recovery. Study more!"
else:
    situation = "FAILED"
    message = "Unfortunately you failed."

print(f"SITUATION: {situation}")
print(message)
print("=" * 50)
