import random

user = input("enter your choice {rock for 'r'}, {paper for 'p'}, {scissors for 's'} :")

if(user ==  'p' or user == 'r' or user =='s'):
  print(f"you chose : {user}")
else:
  raise ValueError("Invalid Input")

opponent_move = ['r','s','p']
opponent = random.choice(opponent_move)
print(f"oponent chose : {opponent}")

def check(opponent, user):

  if (opponent == user):
    return 0

  if(opponent == 'r' and user == 's'):
    return -1

  if(opponent == 'p' and user == 'r'):
    return -1

  if(opponent == 's' and user == 'p'):
    return -1

  return 1


score = check(opponent, user)

if (score == 0):
  print("It's DRAW")
elif (score == 1):
  print("YOU WIN")
elif(score == -1):
  print("YOU LOSE")