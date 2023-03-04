# Slot Machine 🎰
# Codédex

import random

slot_machine_symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

def play_slots():
  results = random.choices(slot_machine_symbols, k=3)
  all_sevens = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

  while not all_sevens:    
    print(f'{results[0]} | {results[1]} | {results[2]}')
    all_sevens = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if all_sevens:
      print("Jackpot!!! 💰")
    else:
      results = random.choices(slot_machine_symbols, k=3)
answer = "Y"

while answer.upper() != "N":
  play_slots()
  answer = input("Keep playing? (Y/N) ")

print("Thanks for playing!")