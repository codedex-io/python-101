# Stock Analysis
# Codédex

stock_prices = [ 95.91, 93.8, 94.38, 96.27, 96.42, 95.54, 95.13, 93.89, 90.11, 91.05, 92.39, 95.23, 95.87, 96.35, 95.96, 97.44, 96.58, 98.23, 98.64, 100.72 ]

def price_at(i):
    return stock_prices[i-1]

def max_price(a, b):
    mx = 0
    for i in range(a, b):
        mx = max(mx, price_at(i))
    return mx

def min_price(a, b):
    mn = price_at(a)
    for i in range(a, b):
        mn = min(mn, price_at(i))
    return mn

print(max_price(1, 21))
print(min_price(10, 20))
print(price_at(3))
