# 99 Bottles of Beer 🍻
# Codédex

for i in range(99, 0, -1):   
  if i > 1:
    print(f'{i} bottles of beer on the wall')
    print(f'{i} bottles of beer')
    print(f'Take one down, pass it around')
    print(f'{i-1} bottles of beer on the wall\n')
  else:
    print(f'{i} bottle of beer on the wall')
    print(f'{i} bottle of beer')
    print(f'Take one down, pass it around')
    print(f'No more bottles of beer on the wall\n')
