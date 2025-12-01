'''
Classify a character as: vowel, consonant, digit, special character
Question: Take a single character and classify it using conditions.
Test Cases:
Input: 'a' → Output: Vowel
Input: '@' → Output: Special Character
'''

ch = input("Enter a character: ")

vowels = "aeiouAEIOU"

if ch.isdigit():
    print("Digit")

elif ch.isalpha():
    if ch in vowels:
        print("Vowel")
    else:
        print("Consonant")

else:
    print("Special Character")