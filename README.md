# Task#1: Write a Python program to check if a number is even or odd

## ✅ How it works:

1. % is the modulus operator, which gives the remainder when one number is divided by another.

2. num % 2 == 0 means the number is divisible by 2 → even.

3. If the remainder is not 0 → odd.

4. End

✅ Examples

Enter a number: 7 , 7 is odd.

Enter a number: 12 , 12 is even.

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

✅ Examples

Enter a non-negative integer: 5
The factorial of 5 is 120

Enter a non-negative integer: 0 , The factorial of 0 is 1

---------------------

# Task#3: Write a Python program to check if a number is prime

## ✅ How it works:

A prime number is a number greater than 1 and divisible only by 1 and itself.

We check divisibility from 2 to sqrt(num) because a larger factor would have a corresponding smaller factor.

If any divisor is found → not prime.

If loop completes without breaking → prime.

📌 Notes:

1, 0, and negative numbers are not prime.

✅ Example

Enter a number: 7
7 is a prime number.

Enter a number: 10 , 10 is not a prime number.

---------------------

# Task#4: Write a Python program to reverse a string

## ✅ How it works:

1. Read the string from the user and store it in variable text

2. Initialize an empty string reversed_text

3. Repeat the following steps for each character char in text (from left to right):

4. Set reversed_text = char + reversed_text (This adds the current character to the front of the reversed string)

5. After the loop ends, reversed_text will contain the reversed string

6. Print reversed_text

7. End

✅ Example

Input: "hello" , Output: "olleh"

📌 What happens exactly?

If text = "hello":

1st Iteration:	'h'	'h'

2nd Iteration:	'e'	'eh'

3rd Iteration:	'l'	'leh'

4th Iteration:	'l'	'lleh'

5th Iteration:	'o'	'olleh'

So the first time the loop runs, char will be the first character of the string.

---------------------