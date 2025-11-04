# This script calculates the factorial of a non-negative integer provided by the user.

# Prompt the user to enter a non-negative integer
num = int(input("Enter a non-negative integer (0-20): "))

# Initialize factorial result
factorial = 1

# Check for negative input
if num < 0:
    print("❌ Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate factorial using a loop
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
