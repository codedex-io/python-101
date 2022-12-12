# Sorting Hat 🧙‍♂️
# Codédex

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print('Q1) Do you like Dawn or Dusk?')
q1=int(input('1) Dawn  \n2) Dusk\n'))
if q1==1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif q1==2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print('Wrong Input')


print('Q2) When I’m dead, I want people to remember me as:')
q2=int(input('1) The God \n2) The Great \n3) The Wise \n4) The Bold\n'))
if q2==1:
    Hufflepuff = Hufflepuff + 1
elif q2==2:
    Slytherin = Slytherin + 1
elif q2==3:
    Ravenclaw = Ravenclaw + 1
elif q2==4:
    Gryffindor = Gryffindor +1
else:
    print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?')
q3=int(input('1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n'))
if q3==1:
    Slytherin = Slytherin + 1
elif q3==2:
    Hufflepuff = Hufflepuff + 1
elif q3==3:
    Ravenclaw = Ravenclaw + 1
elif q3==4:
    Gryffindor = Gryffindor + 1
else:
    print('Wrong Input')

print('Gryffindor: ' ,Gryffindor )
print('Ravenclaw: ' ,Ravenclaw)
print('Hufflepuff: ' ,Hufflepuff)
print('Slytherin: ' ,Slytherin)

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print('Gryffindor')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw >  Slytherin:
    print('Ravenclaw')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('Hufflepuff')
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print('Slytherin')
else:
    print('You belong to no place')
