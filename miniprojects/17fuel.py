# ✅ 17. Fuel Consumption Tracker

# Scenario: Monitor fuel usage and alert user.
# Requirements:
# Input: Daily fuel consumption (list of 7).
# Use for loop to sum total.
# Use if to print alert if total > 50 liters.

fuel_consumption = []

print("Enter fuel consumption (in liters) for 7 days:")

for day in range(1, 8):
    liters = float(input(f"Day {day}: "))
    fuel_consumption.append(liters)

total_fuel = 0
for consumption in fuel_consumption:
    total_fuel += consumption
    
print(f"\nTotal fuel consumed in 7 days: {total_fuel:.2f} liters")

if total_fuel > 50:
    print("Alert: Fuel consumption is over 50 liters!")
else:
    print("Fuel consumption is within the safe limit.")
