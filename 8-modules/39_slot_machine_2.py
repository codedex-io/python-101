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
  print(f'{results[0]} | {results[1]} | {results[2]}')
  win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

  if win:
    print('Jackpot!!! 💰')
  else:
    print('No jackpot this time. 😢')

answer = ''

while answer.upper() != 'N':
  play()
  answer = input('Keep playing? (Y/N) ')

print('Thanks for playing!')
