# Pythagorean Theorem 📐
# Codédex

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > 0 and b > 0:
    c = (a**2 + b**2) ** 0.5
    print("Hypotenuse is:", c)
else:
    print("Please enter positive numbers")
