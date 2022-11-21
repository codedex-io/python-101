# Drive Thru
# Codédex

def get_item(x):
    if x == 1:
        return '🍔 Cheeseburger'
    elif x == 2:
        return '🍟 Fries'
    elif x == 3:
        return '🥤 Soda'
    elif x == 4:
        return '🍦 Ice Cream'
    elif x == 5:
        return '🍪 Cookie'
    else:
        return "invalid option"

def welcome():
    print('Welcome to The Sonny Restaurant! What would you like to order')

welcome()
option = int(input('What would you like to order? '))
print(get_item(option))
