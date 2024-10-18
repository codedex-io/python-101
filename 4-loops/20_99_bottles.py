# 99 Bottles of Beer 🍻
# Codédex

for i in range(99, 0, -1):
  if(i>1):
      s = 's'
  else:
      s =''
  print(f'{i} bottle{s} of beer on the wall')
  print(f'{i} bottle{s} of beer')
  print('Take one down, pass it around')
  if i-1 == 0:
    print('No more bottles of beer on the wall,')
    print('no more bottles of beer.')
    print('We\'ve taken them down')
    print('and passed them around;')
