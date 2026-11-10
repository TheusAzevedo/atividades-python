# ==============================================
# QUESTION 03 - Simple registration system
# ==============================================

# List to store the registrations
people = []

# Registration of 5 people
print("=== PEOPLE REGISTRATION ===\n")
for i in range(1, 6):
    print(f"Person {i}:")
    name = input("  Name: ")
    
    # Age validation
    while True:
        try:
            age = int(input("  Age: "))
            if age < 0:
                print("  Age cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("  Please enter a valid integer for age.")
    
    city = input("  City: ")
    
    # Creates a dictionary to store the person's data
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    # Adds to the list
    people.append(person)
    print()

# Finds the oldest and youngest person using lambda
oldest_person = max(people, key=lambda p: p["age"])
youngest_person = min(people, key=lambda p: p["age"])

# Calculates the average age
age_sum = sum(person["age"] for person in people)
average_age = age_sum / len(people)

# Displays all registrations
print("="*50)
print("REGISTRATION LIST:")
print("="*50)
for i, person in enumerate(people, 1):
    print(f"{i}. Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

# Displays the requested information
print("\n" + "="*50)
print(f"Oldest person: {oldest_person['name']} ({oldest_person['age']} years old)")
print(f"Youngest person: {youngest_person['name']} ({youngest_person['age']} years old)")
print(f"Group average age: {average_age:.2f} years old")
print("="*50)

'''Registration: For loop from 1 to 5 to register 5 people. 

Data input: For each person, requests name, age, and city. 

Validation: Checks if the age is a positive integer. 

Storage: Each person is stored as a dictionary with 'name', 'age', and 'city' keys. 

Analysis: 

Oldest: Uses max() with key=lambda p: p["age"] to find the person with the highest age. 

Youngest: Uses min() with key=lambda p: p["age"]. 

Average: Sums all ages and divides by the total. 

Output: Displays all registered people and statistics. '''