
# ---------
# PART 1  |
# ---------
word = 'supercalifragilisticexpialidocious-'

# Write a loop that prints out each char from word(str)
for letter in word:
    print(letter)

# Write a while look that does the same
index = 0
while index < len(word):
    print(word[index])
    index += 1

# ---------
# PART 2  |
# ---------

# Create a while loop that prints even numbers, given the start is 100, the end is 140. (print 140)
start = 100
end = 140
while start <= end:
    print(start)
    start += 2

# Write a for loop that does the same thing with range
for num in range(100, 141, 2):
    print(f"range: {num}")


# ---------
# PART 3  |
# ---------
# Write a loop that asks user for a password.
# Loop will continue UNTIL user enters password.
pass_phrase = input('Enter passphrase(sillygoose): ').lower()
while pass_phrase != 'sillygoose':
    print('Try again! Passphrase is sillygoose.')
    pass_phrase = input('Enter passphrase(sillygoose): ').lower()
