# The Cyclone 🎢
# Codédex

while True:
  try:
    height = int(input('What is your height (cm)? '))
    credits = int(input('How many credits do you have? '))
    break;
  except ValueError:
    print('Please answer with integer values')

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif credits < 10 and height >= 137:
  print("You don't have enough credits to ride.")
else:
  print("You have not met either requirement.")
