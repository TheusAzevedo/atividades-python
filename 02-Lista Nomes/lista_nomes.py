print("=" * 50)
print("NAME LIST")
print("=" * 50)

names = []

print("\nEnter 5 names:")
for i in range(5):
    name = input(f"Enter the {i+1}º name: ")
    names.append(name)

print("\n" + "=" * 50)

print("REGISTERED NAMES:")
for name in names:
    print(f"  - {name}")

print("\n" + "=" * 50)

total = len(names)
print(f"Total registered names: {total}")

print("=" * 50)

search = input("\nEnter a name to search for: ")

if search in names:
    print(f"'{search}' is on the list!")
    position = names.index(search)
    print(f"Position: {position + 1} place")
else:
    print(f"'{search}' is NOT on the list!")

print("=" * 50)
