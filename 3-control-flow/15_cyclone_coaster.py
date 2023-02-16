# Cyclone Coaster 🎢
# Codédex

myHeight = 150
withTallerPerson = False

if myHeight >= 200:
  print("Enjoy the ride!")

if myHeight < 200:
  if myHeight < 100 or not withTallerPerson:
    print("You're not tall enough for this ride yet.")
  elif myHeight >= 100 and withTallerPerson:
     print("Enjoy the ride!")