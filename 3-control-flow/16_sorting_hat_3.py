Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#question no.1

print('********** question 1 ***********')
print('Q1) Do you like Dawn or Dusk?')
print("1) Dawn")
print("2) Dusk")
ans = int(input('enter your ans(1,2):'))
if ans ==1:
  Gryffindor = Gryffindor+1
  Ravenclaw = Ravenclaw+1
elif ans==2:
  Hufflepuff = Hufflepuff+1
  Slytherin =  Slytherin+1
else :
  print("Wrong input")

#question no.2

print('********** question 2 ***********')
print('Q2) When I’m dead, I want people to remember me as:')
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
ans = int(input('enter your answer (1-4):'))
if ans == 1:
 Hufflepuff = Hufflepuff+2
elif ans == 2:
 Slytherin = Slytherin+2
elif ans == 3:
  Ravenclaw = Ravenclaw+2
elif ans == 4:
  Gryffindor = Gryffindor+2
else :
   print("Wrong input")


#question no.3

print('********** question 3 ***********')
print('Q3) Which kind of instrument most pleases your ear?:')
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
ans = int(input('enter your answer (1-4):'))
if ans == 1:
  Slytherin = Slytherin+4
elif ans == 2:
  Hufflepuff = Hufflepuff+4
elif ans == 3:
  Ravenclaw = Ravenclaw+4
elif ans == 4:
  Gryffindor = Gryffindor+4
else :
   print("Wrong input")

#score 

print('**** total score of each house ****')
print(f'Gryffindor:{Gryffindor}')
print(f'Ravenclaw:{Ravenclaw}')
print(f'Hufflepuff:{Hufflepuff}')
print(f'Slytherin:{Slytherin}')
