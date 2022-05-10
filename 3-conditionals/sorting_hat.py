# Sorting Hat 🧙‍♂️
# Codédex

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print("===============")
print("The Sorting Hat")
print("===============")

print("Q1) Do you like Dawn or Dusk?")

print("  1) Dawn")
print("  2) Dusk")

answer1 = input("Enter your answer (1-2): ")

if answer1 == "1":
  gryffindor += 1
  ravenclaw += 1
elif answer1 == "2":
  hufflepuff += 1
  slytherin +=1
else:
  print("Invalid input.")