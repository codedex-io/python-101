# Birthday Card 🎂
# Codédex

import random, datetime

bday_messages = [
  'Hope you have a very Happy Birthday! 🎈',
  'It\'s your special day – get out there and celebrate!',
  'You were born and the world got better – everybody wins! Happy Birthday!',
  'Another year of you going around the sun! 🌞'
]

today = datetime.date.today()

my_next_birthday = datetime.date(2023, 4, 5)

days_away = my_next_birthday - today

if my_next_birthday == today:
  print(random.choice(bday_messages))
else:
  print(f'My next birthday is {days_away} away!')