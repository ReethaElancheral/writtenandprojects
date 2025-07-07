# ✅ 10. Online Product Discount Calculator

# Scenario: Apply dynamic discount based on product price.
# Requirements:
# Input: Price of product.
# Use if-elif-else:
# 2000 → 30%, 1000–2000 → 10%, else → no discount.
# Use variables and percentage calculation.


price = float(input("Enter the price of the product: "))

discount = 0
if price > 2000:
    discount = 30
elif 1000 <= price <= 2000:
    discount = 10
else:
    discount = 0


discount_amount = (discount / 100) * price
final_price = price - discount_amount

print(f"Original Price: ₹{price:.2f}")
print(f"Discount Applied: {discount}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Price after Discount: ₹{final_price:.2f}")
