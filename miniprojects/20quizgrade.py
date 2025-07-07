# ✅ 20. Quiz Grader App

# Scenario: Auto-grade a multiple-choice quiz.
# Requirements:
# List of correct answers and user answers.
# Use loop to compare and count correct responses.
# Use if to assign grade based on score.


correct_answers = ['A', 'C', 'B', 'D', 'A']

user_answers = []

print("Enter your answers for 5 questions (A/B/C/D):")
for i in range(5):
    ans = input(f"Q{i+1}: ").upper()
    user_answers.append(ans)

score = 0
for i in range(len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        score += 1

if score == 5:
    grade = 'A+'
elif score >= 4:
    grade = 'A'
elif score == 3:
    grade = 'B'
elif score == 2:
    grade = 'C'
else:
    grade = 'F'


print(f"\nYou scored {score} out of 5.")
print(f"Your grade is: {grade}")
