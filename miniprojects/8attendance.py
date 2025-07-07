# ✅ 8. Attendance Counter


# Scenario: A school wants to track attendance for a week.
# Requirements:
# Input: Attendance for 7 days (P or A).
# Use for loop to count total presents.
# Use if to check if total ≥ 5 → Eligible for exam.
# Use list, string, and if-else.

attendance = []

print("Enter attendance for 7 days (P for Present, A for Absent):")
for i in range(1, 8):
    status = input(f"Day {i}: ").strip().upper()
    if status in ("P", "A"):
        attendance.append(status)
    else:
        print("Invalid input! Marked as Absent by default.")
        attendance.append("A")

total_present = attendance.count("P")

print(f"\n📅 Total Present Days: {total_present}")
if total_present >= 5:
    print("✅ Eligible for Exam")
else:
    print("❌ Not Eligible for Exam")
