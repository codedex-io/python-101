# The Cyclone 🎢
# Codédex

height = 250
credits = 10
with_taller_person = False

if height >= 200 and credits >= 10:
  print("Enjoy the ride!")

if height < 200:
  if height < 100 or not with_taller_person:
    print("You're not tall enough for this ride yet.")
  elif height >= 100 and with_taller_person:
    print("Enjoy the ride!")

if credits < 10:
  print("You don't have enough credits to ride.")
