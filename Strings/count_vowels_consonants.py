# Q: Write a Python program to count vowels and consonants in a string.

text = "Hello World"
vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():  # Only count letters
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("String:", text)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
