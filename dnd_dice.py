import random

# function that takes number of sides and returns a random
# number in that range
def roll_dice(sides):
    return random.randint(1, sides)

# Instruct user to enter the side of dice they wish to roll
while True:
  print('Please enter the type of dice you wish to roll by the number of sides:')
  type_die = int(input())
  print('Your die result is ', end=' ')
  result = roll_dice(type_die)
  print(str(result))
  if type_die == 20:
    if result == 1:
      print('Critical Miss!')
    elif result == 20:
      print('Critical Hit!')
  print('Do you want to roll another die? (y or n)', end=' ')
  play_again = input()
  if(play_again.lower() != 'y'):
      break