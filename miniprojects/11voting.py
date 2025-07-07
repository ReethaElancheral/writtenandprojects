# ✅ 11. Voting Eligibility Checker

# Scenario: A system to check who can vote.
# Requirements:
# Input: Name and age.
# Use if to check if age ≥ 18 → Eligible.
# Use else to say "Not eligible".
# Print formatted message.



name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote yet.")
