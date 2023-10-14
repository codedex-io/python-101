# Countdown 🎂
# Codédex

import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2023, 4, 5)


if next_birthday == today:
  print(bday_messages.random_message)
else:
  days_away = next_birthday - today
  print(f'My next birthday is {days_away.days} days away!')
