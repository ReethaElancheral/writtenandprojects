# ✅ 2. Age Category Classifier

# Scenario: Classify people into categories based on age.
# Requirements:
# Input: Name and age.
# Use if-elif-else:
# <13 → Child, 13–19 → Teen, 20–59 → Adult, ≥60 → Senior.
# Use variables and data type validation.
# Display a proper message with classification.

name = input("Enter your name: ")

age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)

    if age < 13:
        category = "Child"
    elif age <= 19:
        category = "Teen"
    elif age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    print(f"\n{name}, you are classified as a(n): {category}")

else:
    print("Invalid input! Age must be a number.")
