# Calculator 🔢
# Codédex

import math

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def exp(a, b):
  return a ** b

def modulus(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b

def square_root(a):
    if a < 0:
        return "Error! Negative number."
    return math.sqrt(a)

print(add(3, 5))
print(subtract(7, 2))
print(multiply(4, 8))
print(divide(9, 3))
print(exp(2, 3))
print(modulus(10, 3))       
print(floor_divide(10, 3))   
print(square_root(16))
