square = lambda s: s*s
rectangle = lambda l, b: l*b
triangle = lambda b, h: 0.5*b*h

s = float(input("Enter the side of the square: "))
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))

print("Area of Square =", square(s))
print("Area of Rectangle =", rectangle(l, b))
print("Area of Triangle =", triangle(base, h))
