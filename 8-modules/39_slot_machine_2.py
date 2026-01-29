# Slot Machine 🎰
# Codédex

import random

symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

def play():
  results = random.choices(symbols, k=3)
  print(results[0] + ' | ' + results[1] + ' | ' + results[2])
  
  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print('Jackpot! 💰')
  else:
    print('Thank for playing!')

question = input("Do you want to start the game? If yes: Click 'Y' If no: Click 'N'")
while question == 'Y':
  play()
  question = input("Do you want to continue? If yes: Click 'Y' If no: Click 'N'")




