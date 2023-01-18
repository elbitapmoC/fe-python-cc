from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)
print(num)

# Turn that random number into the computer's RPS move
if (num == 1):
    computers_ascii = rock
if (num == 2):
    computers_ascii = paper
if (num == 3):
    computers_ascii = scissors

# Ask a user to enter their move
users_move = int(input('Your move (1-rock, 2-paper, 3-scissors): '))

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if (users_move == 1):
    users_ascii = rock
if (users_move == 2):
    users_ascii = paper
if (users_move == 3):
    users_ascii = scissors

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"Computer played:{computers_ascii}")
print(f"You played:{users_ascii}")

# Figure out who wins and print the result!
if users_move == num:
    print("DRAW!")
elif users_move == 1 and num == 2:
    print("COMPUTER WON!")
elif users_move == 1 and num == 3:
    print("YOU WON!")
elif users_move == 2 and num == 1:
    print("YOU WON!")
elif users_move == 2 and num == 3:
    print("COMPUTER WON!")
elif users_move == 3 and num == 1:
    print("COMPUTER WON!")
elif users_move == 3 and num == 2:
    print("COMPUTER WON!")
