import sys
import random
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

print()
playerChoice = input("Enter.... \n1 for Rock, \n2 for Paper, \n3 for Scissors \n\n")

player = int(playerChoice)

if player < 1 or player > 3:
  sys.exit("You must enter 1, 2 or 3.")

computerChoice = random.choice("123")

computer = int(computerChoice)

print()
print("You chose" + str(RPS(player)).replace('RPS.', ', ') + ".")
print("Python chose" + str(RPS(computer)).replace('RPS.', ', ') + ".")

if(player == 1 and computer == 3):
  print('You win (\\*v*/)!')
elif(player == 2 and computer == 1):
  print('You win (\\*v*/)!')
elif(player == 3 and computer == 2):
  print('You win (\\*v*/)!')
elif(player == computer):
  print('A DRAW (/^o^\\)!')
else:
  print("(\\*^*/)Python wins!")