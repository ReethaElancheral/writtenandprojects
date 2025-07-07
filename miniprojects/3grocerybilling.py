# ✅ 3. Grocery Billing System

# Scenario: A grocery store wants to automate billing.
# Requirements:
# Predefined dictionary: item → price.
# Use list to input selected items.
# Use for loop to calculate total bill.
# If total > ₹1000, apply 10% discount.
# Use conditional logic + f-string for output.


grocery_items = {
    "rice": 50,
    "milk": 25,
    "bread": 30,
    "oil": 150,
    "sugar": 40,
    "eggs": 10,
    "flour": 45,
    "tea": 60
}

selected_items = []
print("Available items:", ', '.join(grocery_items.keys()))
print("Enter 3 items to buy:")

for i in range(3):
    item = input(f"Item {i+1}: ").lower()
    if item in grocery_items:
        selected_items.append(item)
    else:
        print(f"{item} is not available. Skipped.")

total = 0
for item in selected_items:
    total += grocery_items[item]

if total > 1000:
    discount = total * 0.10
    total -= discount
    print(f"\n🎉 You got a 10% discount of ₹{discount:.2f}")

print("\n🧾 Bill Summary:")
for item in selected_items:
    print(f"{item.capitalize():<10} - ₹{grocery_items[item]}")

print(f"Total Amount: ₹{total:.2f}")
