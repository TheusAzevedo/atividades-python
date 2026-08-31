print ("=== CALCULATOR ===")

num1 = float(input("Enter the first number: "))
num2 = float (input("Enter the second number: "))

print ("Chose the operation: ")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")

op= input("Enter the operation number: ")

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
    print("Invalad Option")

   
