# Fortune Cookie 🥠
# Codédex

import random

options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)

  if random_fortune == 0:
    option = options[0]
  elif random_fortune == 1:
    option = options[1]
  elif random_fortune == 2:
    option = options[2]
  elif random_fortune == 3:
    option = options[3]
  elif random_fortune == 4:
    option = options[4]
  elif random_fortune == 5:
    option = options[5]
  elif random_fortune == 6:
    option = options[6]
  elif random_fortune == 7:
    option = options[7]
  elif random_fortune == 8:
    option = options[8]
  else:
    option = 'Error'

  print(option)

fortune()
fortune()
fortune()
