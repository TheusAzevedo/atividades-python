print("=" * 40)
print("NUMBER CHECKER")
print("=" * 40)


number = int(input("Enter an integer number: "))

print("\n" + "=" * 40)


if number > 0:
    print(f"The number {number} is POSITIVE")
elif number < 0:
    print(f"The number {number} is NEGATIVE")
else:
    print(f"The number {number} is ZERO")


if number == 0:
    print("The number zero is considered EVEN")
elif number % 2 == 0:
    print(f"The number {number} is EVEN")
else:
    print(f"The number {number} is ODD")

print("=" * 40)
