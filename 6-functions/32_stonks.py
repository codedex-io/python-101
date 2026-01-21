# Stonks 📈
# Codédex

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
def price_at(x):
 price_that_day = stock_prices[x]
 return price_that_day
def max_price(a, b):
  max_stock_price = max(stock_prices[a:b+1])
  return max_stock_price
def min_price(a, b):
   min_stock_price = min(stock_prices[a:b+1])
   return min_stock_price
print("The stock price for the day is " + str(price_at(1)))
print("The maximum stock price is " + str(max_price(0,3)))
print("The minimum stock price is " + str(min_price(0,3)))
print(stock_prices[0:3])
