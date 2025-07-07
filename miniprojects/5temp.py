# ✅ 5. Temperature Converter & Category

# Scenario: Convert temperature and categorize it.
# Requirements:
# Input: Temperature in Celsius.
# Convert to Fahrenheit.
# Use if:
# <20 → Cold, 20–30 → Warm, >30 → Hot.
# Display formatted message with condition.

celsius = float(input("🌡️ Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

if celsius < 20:
    category = "Cold"
elif celsius <= 30:
    category = "Warm"
else:
    category = "Hot"

print(f"\nConverted Temperature: {fahrenheit:.2f}°F")
print(f"🌡️ The weather is classified as: {category}")
