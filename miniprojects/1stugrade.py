# ✅ 1. Student Grade Calculator

# Scenario: A school wants to generate grades based on student scores.
# Requirements:
# Input: Student name and marks in 5 subjects using variables and list.
# Use for loop to calculate total and average.
# Use if-elif-else:
# ≥90 → A, ≥80 → B, ≥70 → C, else → D.
# Output the grade with the student’s name using f-string.

student_name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# Output
print(f"\nStudent Name: {student_name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")
