# ✅ 18. Palindrome Checker

# Scenario: Check if a word is a palindrome.
# Requirements:
# Input: word.
# Use for loop to reverse.
# Use if to compare reversed and original.
# Print if it's a palindrome.


word = input("Enter a word: ").lower()

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word 

if word == reversed_word:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
