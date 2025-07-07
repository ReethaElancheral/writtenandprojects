# ✅ 6. Bank Withdrawal Simulator


# Scenario: A bank app wants to check balance before withdrawal.
# Requirements:
# Input: Initial balance and withdrawal amount.
# Use if to check if sufficient balance exists.
# Use else to print error if not enough balance.
# Use variables and arithmetic.

balance = float(input("Enter your initial bank balance: ₹"))
withdraw = float(input("Enter amount to withdraw: ₹"))

if withdraw <= balance:
    balance -= withdraw
    print(f"\n✅ Withdrawal of ₹{withdraw} successful.")
    print(f"💰 Remaining Balance: ₹{balance:.2f}")
else:
    print(f"\n❌ Insufficient funds! You only have ₹{balance:.2f}")
