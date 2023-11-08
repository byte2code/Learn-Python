
class Area:
    def __init__(self):
        pass

    @staticmethod
    def circle_area(radius):
        return (22/7) * (radius ** 2)

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def rectangle_area(length, width):
        return length * width

area = Area()

# Calculate the area of a circle
circle_area = area.circle_area(5)
print(f"Area of the circle: {circle_area}")

# Calculate the area of a triangle 
triangle_area = area.triangle_area(6, 4)
print(f"Area of the triangle: {triangle_area}")

# Calculate the area of a rectangle
rectangle_area = area.rectangle_area(8, 3)
print(f"Area of the rectangle: {rectangle_area}")
