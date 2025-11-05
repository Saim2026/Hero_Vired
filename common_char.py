# This program counts & prints the number of common characters in two given strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = ""

for char in str1:
    if char in str2 and char not in common:
        common += char

if common:
    print("Common characters:", common)
else:
    print("No common characters found.")
