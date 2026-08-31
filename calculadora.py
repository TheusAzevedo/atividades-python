print ("=== CALCULATOR ===")

num1 = float(input("Enter the first number: "))
num2 = float (input("Enter the second number: "))

print ("Choose the operation: ")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")

op= input("Enter the operation number: ")

if op == "1":
    result = num1 + num2
    print(f"{num1:.2f} + {num2:.2f} = {result:.2f}")

elif op == "2":
    result = num1 - num2
    print(f"{num1:.2f} - {num2:.2f} = {result:.2f}")

elif op == "3":
    result = num1 * num2
    print(f"{num1:.2f} * {num2:.2f} = {result:.2f}")

elif op == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1:.2f} / {num2:.2f} = {result:.2f}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid Option")

   
