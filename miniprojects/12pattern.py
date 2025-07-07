# ✅ 12. Number Pattern Generator

# Scenario: Generate a triangle pattern using a loop.
# Requirements:
# Input: Number of rows.
# Use nested for loop to print:
# 1  
# 1 2  
# 1 2 3  


rows = int(input("Enter the number of rows: "))


for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  
