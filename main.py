
import random
from game_data import data
from art import logo, vs
from replit import clear
compare_A =random.choice(data)
compare_B = random.choice(data)

current_score = 0
game_should_continue = True
while game_should_continue :
  if compare_A == compare_B :
    compare_B = random.choice(data) 
  print(f"{compare_A['name']},{compare_A['description']}, from {compare_A['country']}")
  print(vs)
  print(f"{compare_B['name']},{compare_B['description']}, from {compare_B['country']}")

  question = input("Who has more follwers? A or B ")
  if question == 'A' :
    if compare_A['follower_count'] > compare_B['follower_count'] :
      current_score += 1
      compare_B = random.choice(data)
      print(f"You are right.Current score {current_score}")
    else:
      print(f"Sorry,that's wrong.Final score {current_score}")
      break
  else:
    if compare_B['follower_count'] > compare_A['follower_count'] :
      current_score += 1
      compare_A = compare_B
      compare_B = random.choice(data)
      print(f"You are right.Current score {current_score}")
    else:
      print(f"Sorry,that's wrong.Final score {current_score}")
      break
  


  
