# Drive-Thru 🚙
# Codédex

menu = ['Cheeseburger', 'Fries', 'Soda', 'Ice Cream', 'Cookie']

def get_item(i):
  return(menu[i - 1])

def welcome():
  print("Welcome! Here is our menu:")
  print(menu)

welcome()

order = int(input("What would you like to order? "))
if order > 5:
  print("Invalid order.")
else:
  print(get_item(order))
