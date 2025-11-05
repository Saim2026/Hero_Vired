# This program checks if the input string is a palindrome.
text = input("Enter a string: ")

clean_text = text.replace(" ", "").lower()
reversed_text = ""

for char in clean_text:
    reversed_text = char + reversed_text

if clean_text == reversed_text:
    print("✅ It is a palindrome!")
else:
    print("❌ It is not a palindrome.")
