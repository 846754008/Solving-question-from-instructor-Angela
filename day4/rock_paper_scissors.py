rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock, paper, scissors]

users = int(input("What do you want to choose? type 0 for Rock, 1 for Paper, or 2 for scissors. \n"))

if users > 2 or users < 0:
  print("You Lost! You enter a wrong number")

if users == 0:
  print(choice[0])
elif users == 1:
  print(choice[1])
elif users == 2:
  print(choice[2])
print("Computer: ")

import random
computer_choice = random.randint(0,2)

print(computer_choice)
if computer_choice == 0:
    print(choice[0])
elif computer_choice == 1:
  print(choice[1])
elif computer_choice == 2:
  print(choice[2])

if users == 0 and computer_choice == 2:
  print("You Win!")
elif users == 0 and computer_choice == 1:
  print("You Lost!")
elif users == 1 and computer_choice == 0:
  print("You Win!")
elif users == 1 and computer_choice == 2:
  print("You Lost!")
elif users == 2 and computer_choice == 1:
  print("You Win!")
elif users == 2 and computer_choice == 0:
  print("You Lost!")
elif users == computer_choice:
  print("Tied!")
