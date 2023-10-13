# Currency 💵
# Codédex

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21
# Round to the nearest cent
total = (int(100 * total - 0.5) + 1) / 100.0

print('You have $' + str(total) + ' in USD.')
