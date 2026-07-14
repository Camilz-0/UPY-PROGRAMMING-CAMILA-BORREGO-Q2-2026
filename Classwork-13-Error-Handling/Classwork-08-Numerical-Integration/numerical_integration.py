# Numerical Integration Tool
import math

# INPUT
a = input("Enter the left interval limit (a): ")
b = input("Enter the right interval limit (b): ")
f_x = input("Enter the function in terms of x (e.g., x**2): ")
method = input("Select calculation method (LRM, RRM, MRM): ").upper()

a = float(eval(a.replace("pi", str(math.pi))))
b = float(eval(b.replace("pi", str(math.pi))))

# PROCESS
n = 1000
h = (b - a) / n
area = 0.0

if method == "LRM":
    offset = 0.0
elif method == "RRM":
    offset = h
elif method == "MRM":
    offset = h / 2.0
else:
    offset = 0.0

for i in range(n):
    xi = a + (i * h) + offset
    height = float(eval(f_x.replace("x", f"({xi})")))
    area += height * h

# OUTPUT
print(f"The integration of {f_x} using {method} is: {area:.4f}")