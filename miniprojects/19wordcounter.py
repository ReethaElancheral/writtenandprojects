# ✅ 19. Word Frequency Counter

# Scenario: Count frequency of characters in a word.
# Requirements:
# Input: a word.
# Use dictionary + for loop to count each character.
# Use conditional logic to add/update count.

word = input("Enter a word: ").lower()

frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
