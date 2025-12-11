# Example Practice:
# Ask the user for a word.
word = input("Enter a word: ")
# Use a for loop to print each letter on a new line.
for i in word:
    print(i)
# Challenge:
# Count how many vowels are in the word.
vowels = ["a", "e", "i", "o" ,"u", "A", "E", "I", "O", "U"]
num = 0
for letter in word:
    if letter in vowels:
        num += 1
print(num)