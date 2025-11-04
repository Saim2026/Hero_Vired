# Task#1: Write a Python program to check if a number is even or odd

## ✅ How it works:

1. % is the modulus operator, which gives the remainder when one number is divided by another.

2. num % 2 == 0 means the number is divisible by 2 → even.

3. If the remainder is not 0 → odd.

---------------------

# Task#2: Write a Python program to find the factorial of a number using a loop:

## ✅ How it works:

1. Factorial of a number n is calculated as:
n! = n × (n-1) × (n-2) × ... × 1

2. Initialize factorial = 1 because multiplying by 1 doesn’t change the value.

3. Use a loop from 1 to num to multiply the values step by step.

    📌Special cases:

    0! = 1

    Factorial is not defined for negative numbers.

---------------------

# Task#3: Write a Python program to check if a number is prime

## ✅ How it works:

A prime number is a number greater than 1 and divisible only by 1 and itself.

We check divisibility from 2 to sqrt(num) because a larger factor would have a corresponding smaller factor.

If any divisor is found → not prime.

If loop completes without breaking → prime.

📌 Notes:

1, 0, and negative numbers are not prime.

---------------------