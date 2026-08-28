print ("=== CALCULATOR ===")

num1 = float(input("Enter de first number: "))
num2 = float (input("Enter de second number: "))

print ("Chose the operation: ")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")

op= input("Enter the opretation number: ")

if op == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif op == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif op == "3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif op == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invaladid Option")

   