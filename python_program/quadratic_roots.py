# Check Quadratic Equation Roots: Determine the roots of a quadratic equation. 

import math
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    # x = (-b ± √(b² - 4ac)) / (2a)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)
a = 1
b = 2
c = 1

roots = quadratic_roots(a,b,c)
print(f"Roots of equation {a}x^2 + {b}x + {c}:", roots)