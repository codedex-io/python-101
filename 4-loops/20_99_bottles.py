# 99 Bottles of Beer 🍻
# Codédex

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  if i-1 == 0:
    print('No more bottles of beer on the wall,')
    print('no more bottles of beer.')
    print('We\'ve taken them down')
    print('and passed them around;')
