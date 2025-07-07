# ✅ 9. Bill Splitter Between Friends

# Scenario: A group of friends want to split a dinner bill.
# Requirements:
# Input: Total bill and number of friends.
# Use variables for calculation.
# Use if to check if friends ≥ 1, else show error.
# Print per-head contribution.

total_bill = float(input("Enter total bill amount: ₹"))

num_friends = int(input("Enter number of friends: "))

if num_friends >= 1:
    per_head = total_bill / num_friends
    print(f"\nEach friend should pay: ₹{per_head:.2f}")
else:
    print("❌ Error: Number of friends must be at least 1.")
