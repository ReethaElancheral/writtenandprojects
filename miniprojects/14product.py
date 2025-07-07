# ✅ 14. Product Search Tool

# Scenario: Search if a product is in stock.
# Requirements:
# Predefined list of products.
# Input: Product to search.
# Use for loop + if to find match.
# If found → "Available", else → "Out of stock".


products = ["laptop", "mouse", "keyboard", "monitor", "printer"]

search_product = input("Enter the product to search: ").lower()

found = False
for product in products:
    if product == search_product:
        found = True
        break

if found:
    print(f"{search_product.title()} is Available.")
else:
    print(f"{search_product.title()} is Out of stock.")
