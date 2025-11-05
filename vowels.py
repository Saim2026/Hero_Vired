# This program counts & prints the number of vowels in a given string.
text = input("Enter a string: ")

vowels = "aeiou"
count = 0
found_vowels = ""  # to store the vowels found

for char in text.lower():
    if char in vowels:
        count += 1
        if char not in found_vowels:  # to avoid duplicates
            found_vowels += char

print("Number of vowels:", count)
print("Vowels present:", found_vowels)
