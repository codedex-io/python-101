# The Cyclone 🎢
# Codédex

is_open = True

height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

tall_enough = height >= 137
not_enough_credits = credits < 10

if not is_open:
  print("Sorry! The ride is currently closed!")
elif not tall_enough or not_enough_credits:
  print("You are either not tall enough to ride or you don't have enough credits.")
else:
  print("Enjoy the ride!")
