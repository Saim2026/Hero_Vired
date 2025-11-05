# This Program to check if a number is prime

num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Check divisibility
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
