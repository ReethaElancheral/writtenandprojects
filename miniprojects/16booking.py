# ✅ 16. Room Booking Price Calculator

# Scenario: Hotel room booking system with discount logic.
# Requirements:
# Input: Room type and nights stayed.
# Use if-else for pricing:
# Standard: ₹1000, Deluxe: ₹1500.
# If nights > 3 → 20% discount.


room_type = input("Enter room type (Standard/Deluxe): ").strip().lower()
nights = int(input("Enter number of nights stayed: "))

if room_type == "standard":
    price_per_night = 1000
elif room_type == "deluxe":
    price_per_night = 1500
else:
    print("Invalid room type entered.")
    exit()

total_price = price_per_night * nights

if nights > 3:
    discount = 0.20 * total_price
else:
    discount = 0

final_price = total_price - discount

print(f"Room Type: {room_type.title()}")
print(f"Nights Stayed: {nights}")
print(f"Total Price (before discount): ₹{total_price:.2f}")
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Price to Pay: ₹{final_price:.2f}")
