# ✅ 15. Topper Finder in a Class

# Scenario: Find student with highest marks.
# Requirements:
# Dictionary: name → marks.
# Use for loop to find max marks and topper name.
# Use conditional logic inside loop.

# Topper Finder in a Class


students = {
    "Nisha": 85,
    "Reetha": 92,
    "Mannavan": 78,
    "Geetha": 95,
    "Karthiga": 88
}

topper_name = ""
max_marks = -1

for name, marks in students.items():
    if marks > max_marks:
        max_marks = marks
        topper_name = name

print(f"The topper is {topper_name} with {max_marks} marks.")
