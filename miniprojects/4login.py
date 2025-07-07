# ✅ 4. Simple Login Attempt Tracker

# Scenario: Limit login attempts for user security.
# Requirements:
# Input: username & password.
# Allow 3 attempts using a for loop.
# If credentials match, print "Login Successful", else "Account Locked".
# Use variables and if-else.

correct_username = "admin"
correct_password = "pass123"

for attempt in range(1, 4):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("✅ Login Successful")
        break
    else:
        print(f"❌ Incorrect credentials. Attempt {attempt}/3\n")

else:
    print("🔒 Account Locked due to too many failed attempts.")
