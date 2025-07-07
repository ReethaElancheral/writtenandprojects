# ✅ 7. Even/Odd Number Classifier

# Scenario: Print whether numbers are even or odd.
# Requirements:
# Input: List of 10 numbers.
# Use a for loop + if condition to classify each as even or odd.
# Use list and print() with message formatting.

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

print("\n🔎 Even/Odd Classification:")
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
