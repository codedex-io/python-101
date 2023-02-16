# Cyclone Coaster 🎢
# Codédex

myHeight = 250
credits = 9
withTallerPerson = False

if myHeight >= 200 and credits >= 10:
  breakpoint()
  print("Enjoy the ride!")

if myHeight < 200:
  if myHeight < 100 or not withTallerPerson:
    breakpoint()
    print("You're not tall enough for this ride yet.")
  elif myHeight >= 100 and withTallerPerson:
     breakpoint()
     print("Enjoy the ride!")

if credits < 10:
  print("You don't have enough credits to ride.")