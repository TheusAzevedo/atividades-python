# ==============================================
# QUESTION 01 - Student grade average and status calculator
# ==============================================

# Requests student data
name = input("Enter the student's name: ")

# Requests the three grades with basic validation
try:
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    grade3 = float(input("Enter the third grade: "))
except ValueError:
    print("Error: Please enter valid numbers only.")
    exit()

# Calculates the average
average = (grade1 + grade2 + grade3) / 3

# Determines the student's status
if average >= 7:
    status = "Approved"
elif average >= 5:
    status = "Remedial"
else:
    status = "Failed"

# Displays the final result
print("\n" + "="*40)
print(f"Student's name: {name}")
print(f"Average obtained: {average:.2f}")
print(f"Status: {status}")
print("="*40)

# ==============================================
# TEST EXAMPLE:
# Input: João, 8.5, 7.0, 9.0
# Output: Name: João, Average: 8.17, Status: Approved
# 
# Input: Maria, 5.5, 6.0, 5.5
# Output: Name: Maria, Average: 5.67, Status: Remedial
# 
# Input: Pedro, 3.0, 4.5, 4.0
# Output: Name: Pedro, Average: 3.83, Status: Failed
# ==============================================