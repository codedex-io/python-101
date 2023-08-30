# Drive-Thru 🚙
# Codédex

def get_item(x):
  if x == 1:
    return '🍔 Double-Double'
  elif x == 2:
    return '🍔 Cheeseburger'
  elif x == 3:
    return '🍔 Hamburger'
  elif x == 4:
    return '🍟 French Fries'
  elif x == 5:
    return '🥛 Shakes'
  else:
    return "invalid option"

def welcome():
  print('Welcome to In-N-Out Burger!')
  print('Here\'s the menu:\n')
  print('1️⃣ 🍔 Double-Double   $5.15')
  print('2️⃣ 🍔 Cheeseburger    $3.65')
  print('3️⃣ 🍔 Hamburger       $3.25')
  print('4️⃣ 🍟 French Fries    $2.20')
  print('5️⃣ 🥛 Shakes          $2.85\n')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))
